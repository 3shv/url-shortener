from django.shortcuts import render, redirect

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from uuid import uuid1

from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from .models import Redirect, URLData
from project.settings import DOMAIN
from django.db.models import Q,F

import logging

logger = logging.getLogger(__name__)


@api_view(['POST'])
@renderer_classes((JSONRenderer,))
def create_url(request):
    url = request.data["target_url"]
    slug = uuid1().hex[0:8]
    count = 0
    while count < 10:
        if Redirect.objects.filter(slug=slug).exists():
            slug = uuid1().get_hex()[0:8]
            count += 1
        else:
            break
    slug_obj = Redirect.objects.create(slug=slug)
    URLData.objects.create(target_url=url, slug=slug_obj)
    return Response({"message": "Success", "code": 0, "url": DOMAIN + slug})


@api_view(['POST'])
@renderer_classes((JSONRenderer,))
def configure_url(request):
    data = request.data
    slug = data["slug"] #do cleanUp & validate if required
    try:
        slugObj = Redirect.objects.get(slug=slug)
    except Exception as e:
        logger.error("Input: %s Exception: %s" % (slug,e))
        return Response({"message": "Error with the redirect url slug", "code": 1})

    for config in data["config"]:
            URLData.objects.create(user_agent=config["user_agent"], target_url=config["target_url"], slug=slugObj)
    return Response({"message": "Success", "code": 0})


@api_view(['GET'])
@renderer_classes((JSONRenderer,))
def redirect_url(request, slug):
    try:
        slug_obj = Redirect.objects.get(slug=slug)
        user_agent = request.META['HTTP_USER_AGENT']
        url_obj = None
        try:
            url_obj = URLData.objects.get(slug=slug_obj, user_agent=user_agent)
        except:
            url_obj = URLData.objects.get(slug=slug_obj, user_agent=None) # fall back to default

        target_url = url_obj.target_url
        url_obj.count = F('count') + 1
        url_obj.save(update_fields=['count', ])
        return redirect(target_url)
    except Exception as e:
        logger.error("Input: %s, Exception: %s" % (slug, e))
        return Response(status=status.HTTP_404_NOT_FOUND)









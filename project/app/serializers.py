from .models import *
from rest_framework import serializers, viewsets
from project.settings import DOMAIN
from django.utils.timezone import now


class SlugField(serializers.RelatedField):
    def to_representation(self, value):
        return "%s%s" % (DOMAIN, value)


class RedirectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Redirect
        fields = ('slug', 'created_on')


class URLDataSerializer(serializers.ModelSerializer):
    slug = SlugField(read_only=True)
    time_elapsed = serializers.SerializerMethodField()
    class Meta:
        model = URLData
        fields = ('target_url', 'user_agent', 'count', 'time_elapsed', 'created_on', 'slug')
    def get_time_elapsed(self, obj):
        return (now() - obj.created_on).seconds


# ViewSets define the view behavior.
class URLDataViewSet(viewsets.ModelViewSet):
    queryset = URLData.objects.all()
    serializer_class = URLDataSerializer


class RedirectViewSet(viewsets.ModelViewSet):
    queryset = Redirect.objects.all()
    serializer_class = RedirectSerializer
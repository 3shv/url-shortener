from django.db import models

# Create your models here.

class Redirect(models.Model):
    slug = models.CharField(max_length=60, db_index=True, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.slug

    class Meta:
        ordering = ('created_on', )

class URLData(models.Model):
    target_url = models.CharField(max_length=2083)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    user_agent = models.CharField(max_length=1024, default=None, null=True)
    count = models.PositiveIntegerField(verbose_name="No of redirects", db_index=True, default=0)
    slug = models.ForeignKey(Redirect, )

    def __str__(self):
        return '%s -- %s' % (self.target_url, self.updated_on)

    class Meta:
        ordering = ('updated_on', )

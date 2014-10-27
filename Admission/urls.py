from django.conf.urls import patterns, include, url
from django.views.generic import ListView
from Admission.models import Students

urlpatterns=patterns('',
                     url(r'^', ListView.as_view(
                         queryset=Students.objects.all(),
                         template_name="index.html")),
                     )

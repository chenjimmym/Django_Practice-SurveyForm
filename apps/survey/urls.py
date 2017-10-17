from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'form_processing', views.form_processing),
    url(r'result', views.result),
]
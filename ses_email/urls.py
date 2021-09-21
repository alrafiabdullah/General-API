from django.urls import path

from . import views

urlpatterns = [
    path('send', views.SesEmail.as_view(), name='send'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.gg_view, name='gg_view'),
]

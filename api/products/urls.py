from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('bulk_insert', views.bulk_insert, name='bulk_insert'),
]
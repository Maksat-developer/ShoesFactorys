from django.urls import path, include
from . import views


urlpatterns = [
    path("index/", views.index, name='index'),
    path("community/", views.community, name="community")

]

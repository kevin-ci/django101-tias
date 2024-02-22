from django.urls import path
from . import views

urlpatterns = [
    path("", views.show_blogs, name="show_all"),
    path("create", views.create_blog, name="create"),
]
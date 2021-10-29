from django.urls import path
from . import views
urlpatterns = [
    path("", views.allposts, name="allposts"),
    path("post/<str:pk>/", views.post, name="post"),
    path("post/<str:pk>/likes", views.like, name="like"),
]

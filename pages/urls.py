from django.urls import path
from .views import HomePageView, image_upload_view, ImageListView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("upload/", image_upload_view, name="upload"),
    path("image-list/", ImageListView.as_view(), name="image_list"),
]

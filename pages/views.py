# app/views.py
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from .forms import ImageForm
from .models import Image


class HomePageView(TemplateView):
    template_name = "home.html"


class ImageListView(ListView):
    model = Image
    template_name = "image_list.html"
    context_object_name = "images"


def image_upload_view(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("image_list")
    else:
        form = ImageForm()
    return render(request, "upload.html", {"form": form})

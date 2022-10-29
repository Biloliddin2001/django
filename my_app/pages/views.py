from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Post

# Create your views here.
class Home(TemplateView):
    model = Post
    template_name = "home.html"

class About(TemplateView):
    # model = Post
    template_name = "about.html"
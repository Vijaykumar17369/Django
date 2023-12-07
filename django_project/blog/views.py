from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.


def home(request):
    context  = {
        'posts':Post.objects.all(),
        'title': 'Vijay'
    }
    return render(request, "blog/home.html", context)


def about(request):
    # print("project:", request)
    context= {'project':"request"}
    return render(request,"blog/about.html", context=context)


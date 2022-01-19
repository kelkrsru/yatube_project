from django.shortcuts import render
from django.http.response import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse(status=200, content='Main page')


def group_posts(request, slug):
    return HttpResponse(status=200, content=f"It's group for {slug}")
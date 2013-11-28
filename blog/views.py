# Create your views here.
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render_to_response,render
from models import Blog

def home(request):
    hora = datetime.now()
    template = "index.html"
    blogs = Blog.objects.order_by("timestamp").reverse().all()

    return render(request,template,locals())

def post(request, id_post):
	template = "post.html"
	blog = Blog.objects.get(pk=id_post)
	return render(request,template, locals())
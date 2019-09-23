from django.shortcuts import render, get_object_or_404
from .models import Blog 

def show_all_blogs(request):
	blogs = Blog.objects
	return render(request, 'blogs/home.html', {'blogs': blogs})

def details(request, blog_id):
	detailed_blog = get_object_or_404(Blog, pk=blog_id)
	return render(request, 'blogs/details.html', {'blog': detailed_blog})
from django.shortcuts import render, get_object_or_404
from .models import Blog


def allblogs(request):
    blog = Blog.objects
    '''blogdict = {}
    for i,k in blog:
        blogdict[i]=k
'''
    return render(request, 'blog/allblogs.html', {'blog': blog})

def detail(request, blog_id):
    '''This forms a detailed page for a specific blog'''
    detailblog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'detailblog':detailblog})
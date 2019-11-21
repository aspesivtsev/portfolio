from django.shortcuts import render
from .models import Blog


def allblogs(request):
    blog = Blog.objects
    '''blogdict = {}
    for i,k in blog:
        blogdict[i]=k
'''

    return render(request, "blog/allblogs.html", {'blog': blog})

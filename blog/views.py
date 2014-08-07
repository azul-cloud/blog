from django.shortcuts import render, get_object_or_404

from azulblog.models import Post, Tag


def home(request):
    '''
    show the blog home page
    '''

    return render(request, "blogcontent/home.html", {})


def post(request, **kwargs):
    '''
    show an individual blog post
    '''
    pk = kwargs['pk']
    post = get_object_or_404(Post, id=pk)

    return render(request, "blogcontent/post.html", {'post':post})


def tag(request, **kwargs):
    '''
    show a list of blogs that fit into a certain tag, which is a way to group blog posts together
    '''
    tag = get_object_or_404(Tag, id=kwargs['pk'])

    posts = Tag.get_posts(tag)

    return render(request, "blogcontent/tag.html", {'posts':posts})


def date(request, **kwargs):
    '''
    return a subset of posts based upon a timeframe. Can accept both month and year kwargs
    '''
    posts = Post.objects.all()

    if 'year' in kwargs:
        year = kwargs['year']
        posts = posts.filter(create_date__year=year)

    if 'month' in kwargs:
        month = kwargs['month']
        posts = posts.filter(create_date__month=month)

    return render(request, "blogcontent/time.html", {'month':month, 'year':year, 'posts':posts})
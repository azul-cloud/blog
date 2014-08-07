import os

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.utils.text import slugify

from tinymce.models import HTMLField


class Tag(models.Model):
    '''
    grouping of all the topics that a blog post can be grouped under. Allows
    users to search for a specific type of blog post
    '''
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title

    def get_posts(self):
        '''
        return list of posts that are listed with the tag being queried on
        '''
        from azulblog.models import Post
        posts = self.post_set.all()

        return posts


class Post(models.Model):
    '''
    Data about blog posts. The guts of everything.
    '''
    author = models.ForeignKey(User, related_name="azulblog_author")
    image = models.ImageField(upload_to='azulblog/main',null=True, blank=True)
    title = models.CharField(max_length=50)
    body = HTMLField()
    create_date = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=True)
    tags = models.ManyToManyField(Tag, null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('azulblog-post', kwargs={'pk':self.id, 'slug':slugify(self.title)})
''' Imports '''
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))  # Defining status for the post model.


class Post(models.Model):
    ''' All information needed to create a post '''
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    artist = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    updated_on = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)

    class Meta:
        ''' Define how you want to order the posts on the site '''
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        ''' Add 1 to likes everytime a post is liked by a user '''
        return self.likes.count()


class Comment(models.Model):
    '''  All information needed to create a comment'''
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments"
    )
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ''' Define how you want to order the posts on the site '''
        ordering = ["created_on"]

    def __str__(self):
        ''' How we want the user to see a comment '''
        return f"Comment {self.body} by {self.name}"

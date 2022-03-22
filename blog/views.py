from django.shortcuts import render
from django.views import generic
from .models import Post


class PostList(generic.ListView):
    ''' What the users should be able to see on the site '''
    # What model we are using for this view
    model = Post
    # Only show posts that have a status of published and order
    # them by the date they were created on.
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    # What page users will see this on
    template_name = 'index.html'
    # how many posts we want to see on the page at one time.
    paginate_by = 6

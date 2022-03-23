''' Imports '''
from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post
from .forms import CommentForm


class PostList(generic.ListView):
    ''' What the users should be able to see on the site '''
    # What model we are using for this view
    model = Post
    # Only show posts that have a status of published and order
    # them by the date they were created on.
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    # What page users will see this on
    template_name = 'gallery.html'
    # how many posts we want to see on the page at one time.
    paginate_by = 6


class PostDetail(View):
    ''' Add definition '''
    def get(self, request, slug, *args, **kwargs):
        """ Add description """
        # First filter through the post so we get just the active ones.
        queryset = Post.objects.filter(status=1)
        # Get specific post via its slug.
        post = get_object_or_404(queryset, slug=slug)
        # Then get the approved comments attached to that post.
        comments = post.comments.filter(approved=True).order_by('created_on')
        # Find out if logged in user has liked the post.
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        """ Add description """
        # First filter through the post so we get just the active ones.
        queryset = Post.objects.filter(status=1)
        # Get specific post via its slug.
        post = get_object_or_404(queryset, slug=slug)
        # Then get the approved comments attached to that post.
        comments = post.comments.filter(approved=True).order_by('created_on')
        # Find out if logged in user has liked the post.
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        # Get the data from the form.
        comment_form = CommentForm(data=request.POST)
        # If all fields have been completed, process the comment.
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        # if form is not valid, return empty comment form.
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )


class PostLike(View):
    ''' Add description '''
    def post(self, request, slug):
        ''' Add description'''
        # Get the relevent post.
        post = get_object_or_404(Post, slug=slug)
        # Toggle likes, check if post is already like if it is then then remove the like.
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        # If it hasnt been liked we need to add the like.
        else:
            post.likes.add(request.user)
        # Define where we want to redirect the user when a page is liked or unliked.
        return HttpResponseRedirect(reverse('post_detail', args=[slug]))

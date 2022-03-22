''' Imports '''
from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    ''' Details of what our admin can see/do with our post model '''
    # What we can see when we a shown the list of posts on admin site.
    list_display = ('title', 'slug', 'status', 'created_on')
    # What we can search for on admin site.
    search_fields = ['title', 'content']
    # Generate the slugfield automaticly from the title of a post.
    prepopulated_fields = {'slug': ('title',)}
    # Create a filter box that you can filter posts via their status(Published, Draft).
    # or by the date they were created on.
    list_filter = ('status', 'created_on')
    # Summernote is a simple editor on bootstrap, here we allow the user to use this
    # editor to create content.
    summernote_fields = ('content')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    ''' Details of what our admin can see/do with our post model '''
    # What we can see when we a shown the list of comments on admin site.
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    # filter posts via approved or by the date they were created on.
    list_filter = ('approved', 'created_on')
    # What we can search for on admin site.
    search_fields = ['name', 'email', 'address', 'body']
    # Allow admin to approve comments
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        ''' Define what we want the approve comment function to do '''
        queryset.update(approved=True)

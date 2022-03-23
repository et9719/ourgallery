''' Imports '''
from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    ''' Add description '''
    class Meta:
        ''' Add Description '''
        # Model we want to use.
        model = Comment
        # What feilds we want to use.
        fields = ('body',)

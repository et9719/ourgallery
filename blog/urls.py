''' Imports '''
from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    # path('', name='home'),
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('gallery/', views.PostList.as_view(), name='gallery'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]

from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('detail/<str:slug>', views.BlogDetailView.as_view(), name='blog_detail'),
    path('comment/<str:slug>', views.CreateComment.as_view(), name='comment_create'),
]

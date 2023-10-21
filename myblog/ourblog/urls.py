from django.urls import path
from . import views

urlpatterns = [
    path('article/<int:pk>/', views.article_detail, name='article-detail'),
    path('add_post/', views.add_post, name='add-post'),
]


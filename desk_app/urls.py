from django.urls import path
from . import views

urlpatterns = [
    path('posts/<int:pk>', views.PostsDetailView.as_view(), name='post_detail'),
    path('posts/', views.PostsListView.as_view(), name='post_list'),
    path('posts/<int:pk>/update', views.UpdatePostsView.as_view(), name='post_update'),
    path('posts/create', views.CreatePostsView.as_view(), name='post_create'),
    path('posts/<int:pk>/delete', views.DeletePostsView.as_view(), name='post_delete'),

    path('categories/', views.CategoryListView.as_view(), name='category_list'),
    path('categories/<int:pk>', views.CategoryDetailView.as_view(), name='category_detail'),
    path('categories/<int:pk>/update', views.UpdateCategoryView.as_view(), name='category_update'),
    path('categories/create', views.CreateCategories.as_view(), name='category_create'),
    path('categories/<int:pk>/delete', views.DeleteCategoryView.as_view(), name='category_delete'),

    path('posts/<int:pk>/comments_create', views.CreateComments.as_view(), name='comments_create'),
    path('posts/<int:post_pk>/comments_update/<int:pk>', views.UpdateCommentsView.as_view(), name='comments_update'),
    path('posts/<int:post_pk>/comments_delete/<int:pk>', views.DeleteCommentsView.as_view(), name='comments_delete'),

    path('user_registration/', views.UserRegistrationView.as_view()),
]
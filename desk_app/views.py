from django.shortcuts import render
from django.urls import reverse_lazy

from .models import Posts, Publisher, Categories
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import reverse
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
# Create your views here.


class CreatePostsView(CreateView):
    model = Posts
    fields = '__all__'
    template_name = 'desk_app/form.html'
    success_url = '/posts/{id}'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_name'] = 'Создание поста'
        return context


class PostsDetailView(DetailView):
    model = Posts
    context_object_name = 'posts'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     posts = self.get_object()
    #     comments = posts.comments.all()
    #     context['posts'] = posts
    #     context['comments'] = comments
    #     return context


class PostsListView(ListView):
    model = Posts
    context_object_name = 'posts'


class UpdatePostsView(UpdateView):
    model = Posts
    fields = '__all__'
    success_url = '/posts/'
    template_name = 'desk_app/form.html'


class DeletePostsView(DeleteView):
    model = Posts
    template_name = 'desk_app/form.html'
    success_url = '/posts/'
    permission_required = ''


class CreatePublisherView(CreateView):
    model = Publisher
    fields = '__all__'
    template_name = 'desk_app/form.html'
    success_url = '/publishers/{id}'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_name'] = 'Создание автора'
        return context

#////////////////////////////////////////////////////////////////


class CreateCategories(CreateView):
    model = Categories
    fields = '__all__'
    template_name = 'desk_app/form.html'
    success_url = '{id}'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_name'] = 'Создание категорий'
        return context


class CategoryDetailView(DetailView):
    model = Categories
    context_object_name = 'categories'
    template_name = 'desk_app/category_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = self.get_object()
        posts = categories.posts_for_cat.all()
        context['categories'] = categories
        context['posts'] = posts
        return context


class CategoryListView(ListView):
    model = Categories
    context_object_name = 'categories'
    template_name = 'desk_app/category_list.html'


class UpdateCategoryView(UpdateView):
    model = Categories
    fields = '__all__'
    success_url = '/categories/{id}'
    template_name = 'desk_app/form.html'


class DeleteCategoryView(DeleteView):
    model = Categories
    template_name = 'desk_app/form.html'
    success_url = '/categories/'
    permission_required = ''

#/////////////////////////////////////////////////////////////////////////





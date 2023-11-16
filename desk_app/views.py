from django.shortcuts import render
from django.urls import reverse_lazy

from . import forms
from .models import Posts, Publisher, Categories, Comments
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import reverse
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from .forms import CommentsForm

from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
# Create your views here.


class CreatePostsView(LoginRequiredMixin, CreateView):
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


class UpdatePostsView(UserPassesTestMixin, UpdateView):
    model = Posts
    fields = '__all__'
    success_url = '/posts/'
    template_name = 'desk_app/form.html'

    def test_func(self):
        return self.request.user == self.get_object().publisher.user


class DeletePostsView(UserPassesTestMixin, DeleteView):
    model = Posts
    template_name = 'desk_app/form.html'
    success_url = '/posts/'
    permission_required = ''

    def test_func(self):
        return self.request.user == self.get_object().publisher.user


class CreatePublisherView(LoginRequiredMixin, CreateView):
    model = Publisher
    fields = '__all__'
    template_name = 'desk_app/form.html'
    success_url = '/publishers/{id}'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_name'] = 'Создание автора'
        return context


class UpdatePublisherView(UpdateView):
    model = Publisher
    fields = '__all__'
    template_name = 'desk_app/form.html'
    success_url = '/publishers/{id}'


class PublisherListView(ListView):
    model = Publisher
    context_object_name = 'publishers'


class PublisherDetailView(DetailView):
    model = Publisher
    context_object_name = 'publishers'


class CreateCategories(UserPassesTestMixin, CreateView):
    model = Categories
    fields = '__all__'
    template_name = 'desk_app/form.html'
    success_url = '{id}'

    def test_func(self):
        return self.request.user.is_superuser

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


class UpdateCategoryView(UserPassesTestMixin, UpdateView):
    model = Categories
    fields = '__all__'
    success_url = '/categories/{id}'
    template_name = 'desk_app/form.html'

    def test_func(self):
        return self.request.user.is_superuser


class DeleteCategoryView(UserPassesTestMixin, DeleteView):
    model = Categories
    template_name = 'desk_app/form.html'
    success_url = '/categories/'
    permission_required = ''

    def test_func(self):
        return self.request.user.is_superuser

#/////////////////////////////////////////////////////////////////////////


class CreateComments(CreateView):
    model = Comments
    template_name = 'desk_app/form.html'
    context_object_name = 'comments'
    form_class = CommentsForm

    def get_success_url(self):
        url = reverse('post_detail', kwargs={'pk': self.object.posts.id})
        print(url)
        return url

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.posts = Posts.objects.get(pk=self.kwargs['pk'])
        instance.save()
        self.object = instance
        return HttpResponseRedirect(self.get_success_url())

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     comments = self.get_object()
    #     post = comments.posts.get.filter(id=id)
    #     context['comments'] = comments
    #     context['post'] = post
    #     return context


class UpdateCommentsView(UserPassesTestMixin, UpdateView):
    model = Comments
    fields = '__all__'
    # success_url = 'posts/{id}'
    template_name = 'desk_app/form.html'

    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.posts.id})

    def test_func(self):
        return self.request.user == self.get_object().user


class DeleteCommentsView(UserPassesTestMixin, DeleteView):
    model = Comments
    template_name = 'desk_app/form.html'
    # success_url = '/categories/'
    # permission_required = ''

    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.posts.id})

    def test_func(self):
        return self.request.user == self.get_object().user


class UserRegistrationView(FormView):
    template_name = 'desk_app/form.html'
    form_class = forms.UserRegistrationForm

    def form_valid(self, form):
        return HttpResponse('form valid!')

    def form_invalid(self, form):
        return HttpResponse('form invalid')

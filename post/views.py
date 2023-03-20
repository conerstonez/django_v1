from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import DeleteView, UpdateView

from post.models import Post


# Create your views here.

def hello(request):
    posts = Post.objects.all()
    return render(request, 'post/hello.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post/post-detail.html', {'post': post})


class PostDetailView(DetailView):
    model = Post
    template_name = 'post/post-detail.html'
    context_object_name = 'post'


class PostListView(ListView):
    model = Post
    template_name = 'post/post-list.html'
    context_object_name = 'posts'


class PostCreateView(CreateView):
    model = Post
    template_name = 'post/post-new.html'
    fields = ['title', 'body', 'author']
    success_url = reverse_lazy('home')


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post/post-delete.html'
    success_url = reverse_lazy('home')


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'post/post-update.html'
    fields = ['title', 'body']
    success_url = reverse_lazy('home')


def greet(request):
    return HttpResponse('Welcome to Django!')


def play(request):
    return render(request, 'post/play.html')


def learn(request):
    return render(request, 'learn.html')

#

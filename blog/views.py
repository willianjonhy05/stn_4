from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView, DetailView
from .models import Post, Autor
from django.contrib import messages
from django.urls import reverse
from .forms import PostForm, AutorForm

# Create your views here.

class BlogTemplateView(TemplateView):
    template_name="blog.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()[:7]
        return context

class PostCreateView(CreateView):
    model=Post
    template_name='blog/escrever.html'
    form_class=PostForm

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Post cadastrado com sucesso!")
        return reverse('listar-posts')
    

class AutorCreateView(CreateView):
    model=Autor
    template_name='autor/cadastrar.html'
    form_class=AutorForm

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Autor cadastrado com sucesso!")
        return reverse('listar-autores')
    
class PostListView(ListView):
    model=Post
    template_name='blog/posts.html'
    context_object_name='posts'
    ordering='-titulo'

class AutorListView(ListView):
    model=Autor
    template_name='autor/listar.html'
    context_object_name='autores'
    ordering='-nome'

class PostUpdateView(UpdateView):
    model=Post
    template_name='blog/atualizar.html'
    form_class=PostForm
    pk_url_kwarg='id'

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Post atualizado com sucesso!")
        return reverse('blog')
    
class AutorUpdateView(UpdateView):
    model=Autor
    template_name='autor/atualizar.html'
    form_class=AutorForm
    pk_url_kwarg='id'

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Autor atualizado com sucesso!")
        return reverse('listar-autores')
    
class PostDetailView(DetailView):
    model=Post
    template_name='blog/post.html'
    context_object_name='post'
    pk_url_kwarg='id'

class AutorDetailView(DetailView):
    model=Autor
    template_name='autor/detalhar.html'
    context_object_name='autor'
    pk_url_kwarg='id'

class PostDeleteView(DeleteView):
    model=Post
    template_name='blog/apagar.html'
    pk_url_kwarg='id'

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Post apagado com sucesso!")
        return reverse('listar-posts')
    
class AutorDeleteView(DeleteView):
    model=Autor
    template_name='autor/deletar.html'
    pk_url_kwarg='id'

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Autor apagado com sucesso!")
        return reverse('listar-autores')
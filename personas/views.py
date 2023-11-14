from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView, DetailView
from .models import Midia, Artista, Nerd
from .forms import MidiaForm, ArtistaForm, NerdForm
from django.contrib import messages
from django.urls import reverse

# Create your views here.
class Home(TemplateView):
    template_name = "home.html"

class Sobre(TemplateView):
    template_name = "sobre.html"

class MidiaCreateView(CreateView):
    model=Midia
    template_name='midias/cadastrar.html'
    form_class=MidiaForm

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Filme/Série cadastrado com sucesso!")
        return reverse('listar-midias')
    
class ArtistaCreateView(CreateView):
    model=Artista
    template_name='artistas/cadastrar.html'
    form_class=ArtistaForm

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Artista cadastrado com sucesso!")
        return reverse('listar-artistas')
    
class NerdCreateView(CreateView):
    model=Nerd
    template_name='nerds/cadastrar.html'
    form_class=NerdForm

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Nerd cadastrado com sucesso!")
        return reverse('listar-nerds')
    
class ArtistaListView(ListView):
    model=Artista
    template_name='artistas/listar.html'
    context_object_name='artistas'
    ordering='-nome'

class NerdListView(ListView):
    model=Nerd
    template_name='nerds/listar.html'
    context_object_name='nerds'
    ordering='-nome'

class MidiaListView(ListView):
    model=Midia
    template_name='midias/listar.html'
    context_object_name='midias'
    ordering='-titulo'

class NerdUpdateView(UpdateView):
    model=Nerd
    template_name='nerds/atualizar.html'
    form_class=NerdForm

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Nerd atualizado com sucesso!")
        return reverse('listar-nerds')
    
class MidiaUpdateView(UpdateView):
    model=Midia
    template_name='midias/atualizar.html'
    form_class=MidiaForm

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Filme/Série atualizado com sucesso!")
        return reverse('listar-midias')
    
class ArtistaUpdateView(UpdateView):
    model=Artista
    template_name='artistas/atualizar.html'
    form_class=ArtistaForm

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Artista atualizado com sucesso!")
        return reverse('listar-artistas')
    
class NerdDeleteView(DeleteView):
    model=Nerd
    template_name='nerds/deletar.html'
    pk_url_kwarg='id'

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Nerd deletado com sucesso!")
        return reverse('listar-nerds')
    
class MidiaDeleteView(DeleteView):
    model=Midia
    template_name='midias/deletar.html'
    pk_url_kwarg='id'

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Filme/Série deletado com sucesso!")
        return reverse('listar-midias')
    
class ArtistaDeleteView(DeleteView):
    model=Artista
    template_name='artistas/deletar.html'
    pk_url_kwarg='id'

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Artista deletado com sucesso!")
        return reverse('listar-artistas')
    

class MidiaDetailView(DetailView):
    model=Midia
    template_name='midias/detalhar.html'
    context_object_name='midia'

class ArtistaDetailView(DetailView):
    model=Artista
    template_name='artistas/detalhar.html'
    context_object_name='artista'

class NerdDetailView(DetailView):
    model=Nerd
    template_name='nerds/detalhar.html'
    context_object_name='nerd'
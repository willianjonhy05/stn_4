from django.contrib import admin
from django.urls import path
from .views import PostCreateView, PostDeleteView, PostDetailView, PostListView, PostUpdateView, AutorListView, AutorCreateView, AutorUpdateView, AutorDeleteView, AutorDetailView

urlpatterns = [
    path('', PostListView.as_view(), name='listar-posts'),
    path('escrever/', PostCreateView.as_view(), name='escrever-post'),
    path('atualizar/<int:id>', PostUpdateView.as_view(), name='atualizar-post'),
    path('detalhar/<int:id>', PostDetailView.as_view(), name='detalhar-post'),
    path('deletar/<int:id>', PostDeleteView.as_view, name='apagar-post'),
    path('autores/', AutorListView.as_view(), name='listar-autores'),
    path('autor/cadastrar', AutorCreateView.as_view(), name='cadastrar-autor'),
    path('autor/atualizar/<int:id>', AutorUpdateView.as_view(), name='atualizar-autor'),
    path('autor/deletar/<int:id>', AutorDeleteView.as_view, name='deletar-autor'),
    path('autor/detalhar/<int:id>', AutorDetailView.as_view(), name='detalhar-autor'),
   

]
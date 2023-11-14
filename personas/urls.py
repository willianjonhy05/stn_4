from django.contrib import admin
from django.urls import path
from .views import MidiaCreateView, MidiaDetailView, MidiaDeleteView, MidiaUpdateView, MidiaListView, NerdDeleteView, NerdCreateView, NerdListView, NerdDetailView, NerdUpdateView, ArtistaCreateView, ArtistaDeleteView, ArtistaListView, ArtistaUpdateView, ArtistaDetailView

urlpatterns = [
    path('midias/', MidiaListView.as_view(), name='listar-midias'),
    path('midias/cadastrar', MidiaCreateView.as_view(), name='cadastrar-midia'),
    path('midias/atualizar/<int:id>', MidiaUpdateView.as_view(), name='atualizar-midia'),
    path('midias/detalhar/<int:id>', MidiaDetailView.as_view(), name='detalhar-midia'),
    path('midias/deletar/<int:id>', MidiaDeleteView.as_view, name='deletar-midia'),
    path('nerds/', NerdListView.as_view(), name='listar-nerds'),
    path('nerds/cadastrar', NerdCreateView.as_view(), name='cadastrar-nerd'),
    path('nerds/atualizar/<int:id>', NerdUpdateView.as_view(), name='atualizar-nerd'),
    path('nerds/deletar/<int:id>', NerdDeleteView.as_view, name='deletar-nerd'),
    path('nerds/detalhar/<int:id>', NerdDetailView.as_view(), name='detalhar-nerd'),
    path('artistas/', ArtistaListView.as_view(), name='listar-artistas'),
    path('artistas/cadastrar', ArtistaCreateView.as_view(), name='cadastrar-artista'),
    path('artistas/atualizar/<int:id>', ArtistaUpdateView.as_view(), name='atualizar-artista'),
    path('artistas/deletar/<int:id>', ArtistaDeleteView.as_view, name='deletar-artista'),
    path('artistas/detalhar/<int:id>', ArtistaDetailView.as_view(), name='detalhar-artista'),

    

]
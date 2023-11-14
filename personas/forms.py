from django.forms import ModelForm
from .models import Midia, Artista, Nerd

class MidiaForm(ModelForm):
   
    class Meta:
        model=Midia
        fields='__all__'

class ArtistaForm(ModelForm):
   
    class Meta:
        model=Artista
        fields='__all__'

class NerdForm(ModelForm):
   
    class Meta:
        model=Nerd
        fields='__all__'
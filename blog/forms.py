from django.forms import ModelForm
from .models import Post, Autor

class PostForm(ModelForm):
   
    class Meta:
        model=Post
        fields='__all__'

class AutorForm(ModelForm):
   
    class Meta:
        model=Autor
        fields='__all__'
from django.db import models
from personas.models import Midia, Nerd, Artista

# Create your models here.
class Autor(models.Model):
    nome = models.CharField("Nome", max_length=100)
    sobrenome = models.CharField("Sobrenome", max_length=100)
    email = models.EmailField("Email")
    telefone = models.CharField("Telefone", max_length=20)
    
    def __str__(self):
        return f'{self.nome} {self.sobrenome}'
    
    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"

class Post(models.Model):
    CATEGORIAS = [
        ("Notícias", "Notícias"),
        ("Críticas", "Críticas"),
        ("Entrevistas", "Entrevistas"),
        ("Listas", "Listas"),
        ("Reportagens", "Reportagens")
    ]

    titulo = models.CharField("Titulo", max_length=250)
    subtitulo = models.CharField("Subtitulo", max_length=300)
    conteudo = models.TextField("Conteúdo")
    data_pub = models.DateField("Data de publicação")
    capa = models.ImageField("Foto", upload_to="Capa")
    genero = models.CharField("Categoria", max_length=100, choices=CATEGORIAS)
    autor = models.ForeignKey(Autor, verbose_name="Autor", on_delete=models.CASCADE)
    tags = models.ManyToManyField(Midia, Nerd, Artista, blank=True, null=True)
    

    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
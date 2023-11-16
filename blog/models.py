from django.db import models

# Create your models here.

class Post(models.Model):
    CATEGORIAS = [
        ("Notícias", "Notícias"),
        ("Críticas", "Críticas"),
        ("Entrevistas", "Entrevistas"),
        ("Listas", "Listas"),
        ("Reportagens", "Reportagens")
    ]

    titulo = models.CharField("Titulo", max_length=200)
    conteudo = models.TextField("Conteúdo")
    data_pub = models.DateField("Data de publicação")
    foto = models.ImageField("Foto", upload_to="Capa")
    tags = models.CharField("Categoria", max_length=100, choices=CATEGORIAS)
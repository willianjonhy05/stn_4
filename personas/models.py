from django.db import models
from datetime import date

# Create your models here.

class Midia(models.Model):
    GENERO = [
        ("Comédia", "Comédia"),
        ("Ficção", "Ficção"),
        ("Suspense", "Suspense"),
        ("Aventura", "Aventura"),
        ("Romance", "Romance"),
        ("Animação", "Animação"),
        ("Drama", "Drama"),
        ("Policial", "Policial"),
    ]

    FORMATO = [
        ("Filme", "Filme"),
        ("Série", "Série"),
    ]

    titulo = models.CharField("Título", max_length=100)
    diretor = models.CharField("Diretor", max_length=100)
    sinopse = models.TextField("Sinopse")
    ano = models.PositiveIntegerField("Ano")
    foto = models.ImageField("Foto", upload_to="poster")
    genero = models.CharField("Gênero", max_length=255, choices=GENERO)
    estudios = models.CharField("Estúdio de Produção", max_length=100)
    tipo = models.CharField("Formato", max_length=255, choices=FORMATO)
    volumes = models.PositiveIntegerField("Quantidade de Filmes", blank=True, null=True)
    temporada = models.PositiveIntegerField("Temporadas", blank=True, null=True)
    episodios = models.PositiveIntegerField("Número de Episódios", blank=True, null=True)
    

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Mídia"
        verbose_name_plural = "Mídias"
        ordering = ['titulo']

class Artista(models.Model):

    SEXO = [
        ("Masculino", "Masculino"),
        ("Feminino", "Feminino"),
        ("Outro", "Outro")
    ]


    nome = models.CharField("Nome do Artista", max_length=100)
    data_nasc = models.DateField("Data de Nascimento")

    def calculo_de_idade(self):
        hoje = date.today()
        diferenca = hoje - self.data_nasc
        return round(diferenca.days // 365.25)

    idade = property(calculo_de_idade)
    sexo = models.CharField("Sexo", max_length=100, choices=SEXO)
    foto = models.ImageField("Foto", upload_to='artistas')
    bio = models.TextField("Biografia")
    indicacoes_oscar = models.IntegerField("Indicações ao OSCAR", default=0)
    premios_oscar = models.IntegerField("Premiações do OSCAR", default=0)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Artista"
        verbose_name_plural = "Artistas"
        ordering = ['nome']
   
class Nerd(models.Model):
    nome = models.CharField(max_length=100, default='Nome do Personagem')
    midia = models.ForeignKey(Midia, verbose_name="Mídia", on_delete=models.CASCADE)
    profissao = models.CharField(max_length=100, default='Profissão do Personagem')
    sobre = models.TextField(max_length=900, default='Sobre o personagem')
    foto = models.ImageField(upload_to='avatar', default='default_capa.jpg')
    interprete = models.ManyToManyField(Artista, verbose_name="Interpretes")
    

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Nerd"
        verbose_name_plural = "Nerds"
        ordering = ['nome']




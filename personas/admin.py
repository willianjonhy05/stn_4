from django.contrib import admin
from .models import Artista, Nerd, Midia

# Register your models here.
admin.site.register(Midia)
admin.site.register(Nerd)
admin.site.register(Artista)
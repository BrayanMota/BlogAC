from django.contrib import admin
from .models import Noticia

class NoticiasAdmin(admin.ModelAdmin):
    list_fields = ['__all__']


admin.site.register(Noticia, NoticiasAdmin)
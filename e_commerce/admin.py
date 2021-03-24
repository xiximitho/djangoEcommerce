from django.contrib import admin

# Register your models here.
from .models import Categoria, Produto

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'nome_pagina']
    prepopulated_fields = {'nome_pagina': ('nome',)}

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'nome_pagina', 'preco',
                    'disponivel', 'criado', 'atualizado']
    list_filter = ['disponivel', 'criado', 'atualizado']
    list_editable = ['preco', 'disponivel']
    prepopulated_fields = {'nome_pagina': ('nome',)}
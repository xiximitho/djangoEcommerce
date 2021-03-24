from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=200,
                            db_index=True)
    nome_pagina = models.SlugField(max_length=200,
                                   unique=True)

    class Meta:
        ordering = ('nome',)
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def __str__(self):
        return self.nome

class Produto(models.Model):
    categoria = models.ForeignKey(Categoria,
                                  related_name='produtos',
                                  on_delete=models.CASCADE) # relacionamento 1 pra N (modelo)
    nome = models.CharField(max_length=200, db_index=True)
    nome_pagina = models.SlugField(max_length=200, db_index=True)
    imagem = models.ImageField(upload_to='produtos/%d/%m/%Y', blank=True)

    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    disponivel = models.BooleanField(default=True)
    criado = models.DateTimeField(auto_now_add=True)
    atualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('nome',)
        index_together = (('id', 'nome_pagina'),)

    def __str__(self):
        return self.nome
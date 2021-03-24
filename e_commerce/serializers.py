from rest_framework import serializers
from .models import Produto, Categoria

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ('id', 'categoria', 'nome', 'imagem',
                  'descricao', 'preco', 'disponivel',
                  'criado', 'atualizado', 'nome_pagina')

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ('id', 'nome', 'nome_pagina')
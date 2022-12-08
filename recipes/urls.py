from django.urls import path

from recipes.views import contato, home, sobre

# Criando uma função exemplo:
# no caso deve ser passado um request para a sua execução
# ou seja uma HTTP REQUEST.

# Na ordem de sempre pedir um HTTP REQUEST e sendo retornado
# HTTP RESPONSE

urlpatterns = [
    path('', home),  # Página inicial do site
    path('sobre/', sobre),  # /sobre/
    path('contato/', contato),  # /contato/
]

from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def listar_livros(request):
    livros = [
        {"id": 1, "titulo": "O Senhor dos Anéis"},
        {"id": 2, "titulo": "O Nome do Vento"},
    ]
    return Response(livros)


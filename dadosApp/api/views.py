from rest_framework.views import APIView
from rest_framework.response import Response

class Usuarios(APIView):
    def get(self, request):
        dados = {
            "usuarios": [
                {
                    "nome": "Carlos",
                    "email": "carlos@email.com"
                },
                {
                    "nome": "João",
                    "email": "joão@email.com"
                }
            ]
        }
        return Response(dados)

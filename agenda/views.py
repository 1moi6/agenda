from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
import pandas as pd
from django.conf import settings
from rest_framework.views import APIView
from rest_framework import status
import os

df = None

# Função para carregar o CSV no início da aplicação
def load_csv():
    global df
    csv_path = os.path.join(settings.BASE_DIR, 'static', 'data/solution.csv')
    print(csv_path)
    try:
        df = pd.read_csv(csv_path)
    except FileNotFoundError:
        df = pd.DataFrame()  # Cria um DataFrame vazio se o arquivo não for encontrado

# Carrega o CSV uma vez quando o módulo é importado
load_csv()

@api_view(['GET'])
def Testarotas(request):
    rotas = {'servidor':'rodando'}
    return Response(rotas)


# @permission_classes([IsAuthenticated])
class SearchEntryView(APIView):
    def get(self, request, *args, **kwargs):
        global df
        
        if df.empty:
            return Response({"error": "CSV data not available"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # Obtém os parâmetros da requisição GET (exemplo: /api/search/?name=Alice&age=25)
        query_params = request.query_params

        
        # Filtro dinâmico usando os parâmetros fornecidos
        f_df = df
        f_df = f_df[f_df["time"] == query_params["time"]]
        f_df = f_df[f_df["ips"] == int(query_params["ips"])]
        f_df = f_df[f_df["ops"] == int(query_params["ops"])]
        f_df = f_df[f_df["eps"] == int(query_params["eps"])]
        f_df = f_df[f_df["capacity"] == int(query_params["capacity"])]

        
        
        # Verifica se o DataFrame filtrado não está vazio
        # if f_df.empty:
        #     return Response({"error": "No matching entries found"}, status=status.HTTP_404_NOT_FOUND)
        
        # Converte o DataFrame filtrado em JSON
        result_json = f_df.to_dict(orient='records')
        return Response(result_json, status=status.HTTP_200_OK)
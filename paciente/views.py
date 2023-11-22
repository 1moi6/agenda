# Create your views here.
from rest_framework import status, generics
from rest_framework.views import APIView
from .models import Paciente, ExameConsulta
from .serializers import MeuPacienteSerializer, ExameConsultaSerializer, ExameConsultaSerializer2
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from datetime import datetime

@permission_classes([IsAuthenticated])
class PacienteListCreateView(APIView):
    def post(self, request):
        serializer = MeuPacienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(info_clinica=request.user.cnpj)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        pacientes = Paciente.objects.filter(info_clinica=request.user.cnpj)

        # Serialize os resultados
        serializer = MeuPacienteSerializer(pacientes, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
@permission_classes([IsAuthenticated])
class PacienteDeleteUpdateView(APIView):
    def put(self, request, pk):
        # Recupere o paciente com base no ID
        try:
            paciente = Paciente.objects.get(id=pk,info_clinica = request.user.cnpj)
        except Paciente.DoesNotExist:
            return Response({"error": "paciente não encontrado"}, status=status.HTTP_404_NOT_FOUND)

        # Atualize a consulta/agendamento com os dados fornecidos na solicitação
        serializer = MeuPacienteSerializer(paciente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        # Recupere o paciente com base no ID
        try:
            paciente = Paciente.objects.get(id=pk,info_clinica = request.user.cnpj)
        except Paciente.DoesNotExist:
            return Response({"error": "paciente não encontrado"}, status=status.HTTP_404_NOT_FOUND)

        # Exclua a consulta/agendamento
        paciente.delete()
        return Response({"message": "dados do paciente excluídos com sucesso"}, status=status.HTTP_204_NO_CONTENT)

@permission_classes([IsAuthenticated])
class ExameConsultaCriateListView(APIView):
    def post(self, request, pk):
        # Recupere o paciente com base no ID
        try:
            paciente = Paciente.objects.get(id=pk,info_clinica=request.user.cnpj)
        except Paciente.DoesNotExist:
            return Response({"error": "paciente não encontrado"}, status=status.HTTP_404_NOT_FOUND)

        # Crie uma instância de ExamesConsultas com base nos dados da solicitação
        serializer = ExameConsultaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(paciente=paciente,info_clinica=request.user.cnpj)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, pk):
        # Recupere o paciente com base no ID
        try:
            paciente = Paciente.objects.get(id=pk,info_clinica=request.user.cnpj)
        except Paciente.DoesNotExist:
            return Response({"error": "Paciente não encontrado"}, status=status.HTTP_404_NOT_FOUND)

        # Consulte o banco de dados para obter as consultas e agendamentos do paciente
        consultas_agendamentos = ExameConsulta.objects.filter(paciente=paciente).order_by('-data_agendamento','-hora_agendamento')

        # Serialize os resultados
        serializer = ExameConsultaSerializer(consultas_agendamentos, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
@permission_classes([IsAuthenticated])
class ExameConsultaUpdataDeleteView(APIView):
    def put(self, request, pk, consulta_id):
        print(pk,consulta_id)
        # Recupere o paciente com base no ID
        try:
            paciente = Paciente.objects.get(id=pk,info_clinica = request.user.cnpj)
        except Paciente.DoesNotExist:
            return Response({"error": "paciente não encontrado"}, status=status.HTTP_404_NOT_FOUND)

        # Recupere a consulta/agendamento com base no ID
        try:
            consulta = ExameConsulta.objects.get(id=consulta_id, paciente=paciente)
        except ExameConsulta.DoesNotExist:
            return Response({"error": "consulta/agendamento não encontrado"}, status=status.HTTP_404_NOT_FOUND)

        # Atualize a consulta/agendamento com os dados fornecidos na solicitação
        serializer = ExameConsultaSerializer(consulta, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, consulta_id):
        # Recupere o paciente com base no ID
        try:
            paciente = Paciente.objects.get(id=pk,info_clinica = request.user.cnpj)
        except Paciente.DoesNotExist:
            return Response({"error": "paciente não encontrado"}, status=status.HTTP_404_NOT_FOUND)

        # Recupere a consulta/agendamento com base no ID
        try:
            consulta = ExameConsulta.objects.get(id=consulta_id, paciente=paciente)
        except ExameConsulta.DoesNotExist:
            return Response({"error": "consulta/agendamento não encontrado"}, status=status.HTTP_404_NOT_FOUND)

        # Exclua a consulta/agendamento
        consulta.delete()
        return Response({"message": "consulta/agendamento excluído com sucesso"}, status=status.HTTP_204_NO_CONTENT)
    
@permission_classes([IsAuthenticated])
class AgendaDia(generics.ListAPIView):
    serializer_class = ExameConsultaSerializer2

    def get_queryset(self):
        # Recupere a data de início e fim da requisição GET
        data_inicio = self.request.query_params.get('data_inicio')
        data_inicio = datetime.strptime(data_inicio, "%Y-%m-%d").date()
        data_fim = self.request.query_params.get('data_fim')
        data_fim = datetime.strptime(data_fim, "%Y-%m-%d").date()
        print(data_fim,data_inicio,self.request.user)
        # data_inicio = self.request.data['data_inicio']
        # data_fim = self.request.data['data_fim']


        # Filtrar pacientes com data de atendimento dentro do intervalo especificado
        queryset = ExameConsulta.objects.filter(data_agendamento__gte=data_inicio, data_agendamento__lte=data_fim,info_clinica=self.request.user.cnpj)
        

        return queryset
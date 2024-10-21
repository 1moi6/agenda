from rest_framework import serializers
from .models import Paciente, ExameConsulta


class MeuPacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        exclude =  ["info_clinica"]


class PacienteSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields =  ['nome','cpf','telefone1']

class ExameConsultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExameConsulta
        fields =  "__all__"

class ExameConsultaSerializer2(serializers.ModelSerializer):
    paciente_info = PacienteSerializer2(source='paciente', read_only=True)
    class Meta:
        model = ExameConsulta
        fields = ['paciente','id','data_agendamento', 'hora_agendamento', 'tipo','origem_agendamento', 'medico', 'data_checkin', 'hora_checkin', 'convenio', 'numcarteirinha', 'validade', 'observacoes','status', 'paciente_info']




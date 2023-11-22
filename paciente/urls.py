from django.contrib import admin
from django.urls import path, include
from paciente import views
from .views import PacienteListCreateView, PacienteDeleteUpdateView, ExameConsultaCriateListView, ExameConsultaUpdataDeleteView, AgendaDia

urlpatterns = [
    # path('authteste/', views.RotaAutenticada, name='teste_rota_autenticada'),
    path('pacientes/', PacienteListCreateView.as_view(), name='lista-cria-paciente'),
    path('pacientes/<int:pk>/', PacienteDeleteUpdateView.as_view(), name='atualiza-deleta-apaciente'),
    path('pacientes/<int:pk>/agendamento/', ExameConsultaCriateListView.as_view(), name='cria-lista-agendamento'),
    path('pacientes/<int:pk>/agendamento/<int:consulta_id>/', ExameConsultaUpdataDeleteView.as_view(), name='altualiza-deleta-agendamento'),
    path('agenda/', AgendaDia.as_view(), name='pacientes-filtrados')
]

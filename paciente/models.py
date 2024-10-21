from django.db import models

# Create your models here.
class Paciente(models.Model):
    info_clinica = models.CharField(max_length=20,blank=True)
    nome = models.CharField(max_length=100)
    nascimento = models.DateField(null=True,blank=True)
    idade = models.PositiveIntegerField(blank=True,null=True)
    naturalidade = models.CharField(max_length=100,blank=True)
    nacionalidade = models.CharField(max_length=100,blank=True)
    sexo = models.CharField(max_length=100,blank=True)
    cor = models.CharField(max_length=100,blank=True)
    estadocivil = models.CharField(max_length=100,blank=True)
    profissao = models.CharField(max_length=100,blank=True)
    telefone1 = models.CharField(max_length=100,blank=True)
    telefone2 = models.CharField(max_length=100,blank=True)
    email1 = models.EmailField(blank=True)
    email2 = models.EmailField(blank=True)
    cpf = models.CharField(max_length=100,unique=True)
    rg = models.CharField(max_length=100,blank=True)
    rg_emissor = models.CharField(max_length=100,blank=True)
    cns = models.CharField(max_length=100,blank=True)
    cep = models.CharField(max_length=100,blank=True)
    endereco = models.TextField(blank=True)
    mae = models.CharField(max_length=100,blank=True)
    pai = models.CharField(max_length=100,blank=True)
    responsavel = models.CharField(max_length=100,blank=True)
    observacoes = models.TextField(blank=True)
    def __str__(self):
        return self.nome


class ExameConsulta(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    data_agendamento = models.DateField()
    hora_agendamento = models.TimeField()
    tipo = models.CharField(max_length=100,blank=True)
    origem_agendamento = models.CharField(max_length=100,blank=True)
    medico = models.CharField(max_length=100,blank=True)
    data_checkin = models.DateField(blank=True,null=True)
    hora_checkin = models.TimeField(blank=True,null=True)
    convenio = models.CharField(max_length=100,blank=True)
    numcarteirinha = models.CharField(max_length=100,blank=True)
    validade = models.DateField(blank=True,null=True)
    observacoes = models.TextField(blank=True)
    status = models.CharField(max_length=100,blank=True)
    info_clinica = models.CharField(max_length=20,blank=True)
    def __str__(self):
        return f"Exames e consultas de {self.paciente.nome}"
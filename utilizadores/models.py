from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User 
from candidaturas.models import Candidatura
import string

class Gestor(User):
    def __init__(self):
        super(Gestor, self).__init__()
        is_superuser = True

class Fisioterapeuta(User):
    candidatura = models.ForeignKey(Candidatura)
    
    def __init__(self):
        super(Fisioterapeuta, self).__init__()
        self.email = candidatura.email
        self.username = candidatura.email
        self.password = "password"
        self.first_name = candidatura.nome.split(' ')[0]
        self.last_name = candidatura.nome.split(' ')[-1]


class Paciente(User):
    morada = models.CharField(max_length=300)
    telefone = models.PositiveIntegerField()
    data_nascimento = models.DateField()

class Medico(User):
    morada = models.CharField(max_length=300)
    telefone = models.PositiveIntegerField()


class MedicoForm(ModelForm):
    class Meta:
        model = Medico

class PacienteForm(ModelForm):
    class Meta:
        model = Paciente
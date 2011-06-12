from django.db import models
from django import forms
from django.contrib.auth.models import User, UserManager
from candidaturas.models import Candidatura
import string


class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True, related_name='profile')
    rua = models.CharField(max_length=100)
    cod_postal = models.PositiveIntegerField()
    cidade = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)
    latitude = models.FloatField()
    longitude = models.FloatField()
    telefone = models.PositiveIntegerField()
    data_nascimento = models.DateField()
    candidatura = models.ForeignKey(Candidatura, related_name='profile',
                    null=True, unique=True)


class RfUserForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    data_nascimento = forms.DateField()
    rua = forms.CharField(max_length=100)
    cod_postal = forms.IntegerField()
    cidade = forms.CharField(max_length=50)
    #pais = forms.CharField(max_length=50)
    telefone = forms.IntegerField(min_value=0)
    email = forms.EmailField()

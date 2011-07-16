from django.db import models
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

class Tratamento(models.Model):
    paciente = models.ForeignKey(User, related_name='paciente')
    fisioterapeuta = models.ForeignKey(User, related_name='fisioterapeuta')
    data_inicio = models.DateField(auto_now_add=True)
    data_fim = models.DateField(blank=True, null=True)
		
#	def __unicode__(self):
#	    return self.nome
	
    class Meta:
        ordering = ['data_inicio']


class FichaTratamento(models.Model):
    tratamento = models.ForeignKey(Tratamento)
    nome = models.CharField(max_length=32)
    ficha = models.FileField(upload_to='tratamentos/fichas/%Y/%m/%d',
                            max_length=200)
    data = models.DateTimeField(auto_now=True)

class FichaForm(forms.Form):
    nome = forms.CharField(max_length=32)
    ficha = forms.FileField()
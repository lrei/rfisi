from django.db import models
from django import forms
from geopy import geocoders

class Candidatura(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	data_nascimento = models.DateField()
	rua = models.CharField(max_length=100)
	cod_postal = models.PositiveIntegerField()
	cidade = models.CharField(max_length=50)
	pais = models.CharField(max_length=50)
	latitude = models.FloatField()
	longitude = models.FloatField()
	telefone = models.PositiveIntegerField()
	email = models.EmailField()
	nib = models.CharField(max_length=50)
	nif = models.PositiveIntegerField()
	recibos_verdes = models.BooleanField()
	fotocopia_bi = models.FileField(upload_to='candidaturas/bi/%Y/%m/%d', 
									max_length=200)
	cv = models.FileField(upload_to='candidaturas/cv/%Y/%m/%d',
	                        max_length=200)
	data_candidatura = models.DateTimeField(auto_now=True)
	aceite =  models.BooleanField()
		
	def __unicode__(self):
	    return self.nome
	
	class Meta:
	    ordering = ['data_candidatura']


class CandidaturaForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    data_nascimento = forms.DateField()
    rua = forms.CharField(max_length=100)
    cod_postal = forms.IntegerField()
    cidade = forms.CharField(max_length=50)
    #pais = forms.CharField(max_length=50)
    telefone = forms.IntegerField()
    email = forms.EmailField()
    nib = forms.CharField(max_length=50)
    nif = forms.IntegerField()
    recibos_verdes = forms.BooleanField()
    fotocopia_bi = forms.FileField()
    cv = forms.FileField()

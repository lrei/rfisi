from django.db import models

# Create your models here.

class Candidatura(models.Model):
	nome = models.CharField(max_length=100)
	data_nascimento = models.DateField()
	morada = models.CharField(max_length=300)
	telefone = models.PositiveIntegerField()
	email = models.EmailField()
	nib = models.CharField(max_length=50)
	nif = models.PositiveIntegerField()
	recibos_verdes = models.BooleanField()
	fotocopia_bi = models.FileField(upload_to='candidaturas/bi/%Y/%m/%d', 
									max_length=200)
	cv = models.FileField(upload_to='candidaturas/cv/%Y/%m/%d', max_length=200)
	data_candidatura = models.DateTimeField(auto_now=True)


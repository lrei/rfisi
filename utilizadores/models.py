from django.db import models
from django import forms
from django.contrib.auth.models import User, UserManager
from candidaturas.models import Candidatura
import string


class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True, related_name='profile')
    morada = models.CharField(max_length=300)
    telefone = models.PositiveIntegerField()
    data_nascimento = models.DateField()
    candidatura = models.ForeignKey(Candidatura, related_name='profile',
                    null=True, unique=True)
    

User.profile = property(lambda u: UserProfile.objects.get_or_create(user = 
                                                                    u)[0])

class RfUserForm(forms.Form):
    morada = forms.CharField(max_length=300)
    telefone = forms.IntegerField(min_value=0)
    email = forms.EmailField()
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    data_nascimento = forms.DateField()

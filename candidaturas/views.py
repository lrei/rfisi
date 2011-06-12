from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.template import Template, RequestContext, loader, Context
from candidaturas.models import Candidatura, CandidaturaForm
from django.http import Http404
from utilizadores.models import UserProfile
from utilizadores.views import allowed_chars
from django.contrib.auth.models import User
from geopy import geocoders
#from exceptions import *


def detail(request, candidatura_id):
    c = get_object_or_404(Candidatura, pk=candidatura_id)
    return render_to_response('candidaturas/detail.html',
                                    {'candidatura': c})

def add(request):
    if request.method == 'POST': # If the form has been submitted...
        form = CandidaturaForm(request.POST, request.FILES)
        if form.is_valid():
            c = Candidatura()
            c.first_name = form.cleaned_data['first_name']
            c.last_name = form.cleaned_data['last_name']
            c.data_nascimento = form.cleaned_data['data_nascimento']
            c.rua = form.cleaned_data['rua']
            c.cod_postal = form.cleaned_data['cod_postal']
            c.cidade = form.cleaned_data['cidade']
            #c.pais = form.cleaned_data['pais']
            c.pais = 'Portugal' 
            c.telefone = form.cleaned_data['telefone']
            c.email = form.cleaned_data['email']
            c.nib = form.cleaned_data['nib']
            c.nif = form.cleaned_data['nif']
            c.recibos_verdes = form.cleaned_data['recibos_verdes']
            c.fotocopia_bi = form.cleaned_data['fotocopia_bi']
            c.cv = form.cleaned_data['cv']
            c.aceite =  False
            g = geocoders.Google()
            try:
                place, (lat, lng) = g.geocode(c.rua + " " + \
                                                str(c.cod_postal) + \
                                                " " + c.cidade + ", " + \
                                                 c.pais)
            except:
                return render_to_response('candidaturas/locerror.html',
                                    {'candidatura': c},
                                    context_instance=RequestContext(request))
            c.latitude = lat
            c.longitude = lng
            c.save()
            # Redirect after POST
            return render_to_response('candidaturas/thanks.html',
                                {'candidatura': c},
                                context_instance=RequestContext(request))
    
    else:
        form = CandidaturaForm() # An unbound form

    return render_to_response('candidaturas/add.html', {'form': form},
                                context_instance=RequestContext(request))


def rm(request, candidatura_id):
    c = Candidatura.objects.get(pk=candidatura_id)
    c.delete()
    return HttpResponseRedirect('/candidaturas/')


def approve(request, candidatura_id):
    c = Candidatura.objects.get(pk=candidatura_id)
    new_pass = User.objects.make_random_password(length = 10,
                    allowed_chars = allowed_chars)
                    
    try:
        user = User.objects.create_user(c.email, c.email, new_pass)
        user.first_name = c.first_name
        user.last_name = c.last_name
        user.save()
    except:
        return render_to_response('candidaturas/detail.html',
                                           {'candidatura': c})
    try:
        user_profile = UserProfile(user=user)
        user_profile.data_nascimento = c.data_nascimento
        user_profile.rua = c.rua
        user_profile.cod_postal = c.cod_postal
        user_profile.cidade = c.cidade
        user_profile.pais = c.pais
        user_profile.telefone = c.telefone
        user_profile.candidatura = c
        user_profile.latitude = c.latitude
        user_profile.longitude = c.longitude
        user_profile.save()
    except Exception as e:
        user.delete()
        print e
        return render_to_response('candidaturas/detail.html',
                                        {'candidatura': c})

    c.aceite = True
    c.save()
    
    return HttpResponseRedirect('/candidaturas/')
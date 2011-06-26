from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.template import Template, RequestContext
from django.http import Http404
from utilizadores.models import *
from candidaturas.models import *
from django.contrib.auth.models import User
from geopy import geocoders, distance
import operator
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from django.utils.encoding import *
from tratamentos.models import *

allowed_chars = 'abcdefghjkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789-_.!?'

@login_required
def add(request):
    if request.user.is_superuser is False:
            return render_to_response('utilizadores/permerror.html',
                                    context_instance=RequestContext(request))
    
    if request.method == 'POST': # If the form has been submitted...
        form = RfUserForm(request.POST, request.FILES)
        if form.is_valid():
            new_pass = User.objects.make_random_password(length = 10,
                                        allowed_chars = allowed_chars)
            try:
                user = User.objects.create(
                                        username = form.cleaned_data['email'],
                                        email = form.cleaned_data['email'],
                                        password = new_pass)
                user.first_name = form.cleaned_data['first_name']
                user.last_name = form.cleaned_data['last_name']
                user.save()
            except:
                return render_to_response('utilizadores/add_user.html',
                                    {'form': form},
                                    context_instance=RequestContext(request))
            try:
                user_profile = UserProfile(user=user)
                user_profile.data_nascimento = \
                                        form.cleaned_data['data_nascimento']
                user_profile.telefone = form.cleaned_data['telefone']
                rua = form.cleaned_data['rua']
  
                user_profile.rua = rua
                cod_postal = form.cleaned_data['cod_postal']
                user_profile.cod_postal  = cod_postal
                cidade = form.cleaned_data['cidade']
                user_profile.cidade = cidade
                #pais = form.cleaned_data['pais']
                pais = 'Portugal'
                user_profile.pais = pais
                g = geocoders.Google()
                address = smart_str(rua + " " + str(cod_postal) + " " + \
                                        cidade + ", " + pais,
                                        encoding='utf-8')
                place, (lat, lng) = g.geocode(address)
                user_profile.latitude = lat
                user_profile.longitude = lng
                user_profile.save()
                # Send email notification with password
                #
                #---------- HERE ------------
                #

                # Redirect after POST
                return HttpResponseRedirect('/utilizadores/')
            except:
                user.delete()
                return render_to_response('utilizadores/add_user.html',
                                        {'form': form},
                                    context_instance=RequestContext(request))
            

            
    else:
        form = RfUserForm() # An unbound form

    return render_to_response('utilizadores/add_user.html', {'form': form},
                                context_instance=RequestContext(request))

@login_required
def user_list(request):
    
    if request.user.is_superuser:
        users = User.objects.filter(is_superuser=False,
                                    profile__candidatura__isnull=True)
        return render_to_response('utilizadores/user_list.html',
                                    {'users': users},
                                    context_instance=RequestContext(request))
    elif request.user.get_profile().candidatura:
        tratamentos = Tratamento.objects.filter(fisioterapeuta=request.user)
        users = []
        for tratamento in tratamentos:
            users.append(tratamento.paciente)
        return render_to_response('utilizadores/user_list.html',
                                    {'users': users},
                                    context_instance=RequestContext(request))
        
    
    return render_to_response('utilizadores/permerror.html',
                                    context_instance=RequestContext(request))
    
    

@login_required
def detail(request, user_id):
    u = User.objects.get(pk=user_id)
    p = u.get_profile()
    
    if request.user.is_superuser:
        return render_to_response('utilizadores/detail.html',
                                {'user': u, 'prof': p},
                                context_instance=RequestContext(request))
    elif request.user.get_profile().candidatura:
        tratamentos = Tratamento.objects.filter(paciente=u)
        for tratamento in tratamentos:
            if tratamento.fisioterapeuta == request.user:
                return render_to_response('utilizadores/detail.html',
                                    {'user': u, 'prof': p},
                                    context_instance=RequestContext(request))
    
    return render_to_response('utilizadores/permerror.html',
                                context_instance=RequestContext(request))

@login_required                                                            
def near(request, user_id):
    if request.user.is_superuser is False:
         return render_to_response('utilizadores/permerror.html',
                                    context_instance=RequestContext(request))
         
    u = User.objects.get(pk=user_id)
    n = u.first_name + " " + u.last_name
    coord1 = (u.get_profile().latitude, u.get_profile().longitude)
    users = User.objects.filter(profile__candidatura__isnull=False)
    g = geocoders.Google()
    
    dist = {}
    names = {}
    for user in users:
        if user == u:
            continue
        if user.get_profile() == None:
            continue
        if user.get_profile().candidatura == None:
            continue
        coord2 = (user.get_profile().latitude, user.get_profile().longitude)
        dist[user.id] = distance.distance(coord1, coord2).km
        names[user.id] = user.first_name + " " + user.last_name
        
    # sort the dictionary
    sorted_t = sorted(dist.iteritems(),
                    key=operator.itemgetter(1))
    #sd = dict(sorted_t)
    
    fisioterapeutas = []
    for (key, value) in sorted_t:
        fisioterapeutas.append(FisiDistance(key, names[key],
                                            str(round(value, 2))))
        
    
    return render_to_response('utilizadores/distances.html',
                                {'fisioterapeutas':fisioterapeutas,'user':u, 
                                'prof':user.get_profile()},
                                context_instance=RequestContext(request))
    
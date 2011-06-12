from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.template import Template, RequestContext
from django.http import Http404
from utilizadores.models import *
from candidaturas.models import *
from django.contrib.auth.models import User
from geopy import geocoders, distance
import operator

allowed_chars = 'abcdefghjkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789-_.!?'

def add(request):
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
                place, (lat, lng) = g.geocode(rua + " " + \
                                        str(cod_postal) + \
                                        " " + cidade + \
                                        ", " + pais)
                user_profile.latitude = lat
                user_profile.longitude = lng
                user_profile.save()
            except:
                user.delete()
                return render_to_response('utilizadores/add_user.html',
                                        {'form': form},
                                    context_instance=RequestContext(request))
            

            # Redirect after POST
            return HttpResponseRedirect('utilizadores/thanks.html') 
    else:
        form = RfUserForm() # An unbound form

    return render_to_response('utilizadores/add_user.html', {'form': form},
                                context_instance=RequestContext(request))
def user_list(request):
    users = User.objects.filter(profile__candidatura__isnull=True)
    return render_to_response('utilizadores/user_list.html', {'users': users},
                                context_instance=RequestContext(request))
    
def detail(request, user_id):
    u = get_object_or_404(User, pk=user_id)
    p = u.get_profile()
    return render_to_response('utilizadores/detail.html',{'user': u,
                                                            'prof': p})
                                                                    
def near(request, user_id):
    u = User.objects.get(pk=user_id)
    coord1 = (u.get_profile().latitude, u.get_profile().longitude)
    users = User.objects.filter(profile__candidatura__isnull=False)
    g = geocoders.Google()
    
    dist = {}
    for user in users:
        if user == u:
            continue
        if user.get_profile() == None:
            continue
        if user.get_profile().candidatura == None:
            continue
        coord2 = (user.get_profile().latitude, user.get_profile().longitude)
        dist[user.id] = distance.distance(coord1, coord2).km
    
    # sort the dictionary
    #sd = sorted(dist.items(), key=operator.itemgetter(1))
    
    return render_to_response('utilizadores/distances.html',
                                {'distances':dist},
                                context_instance=RequestContext(request))
    
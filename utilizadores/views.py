from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.template import Template, RequestContext
from django.http import Http404
from utilizadores.models import *
from candidaturas.models import *
from django.contrib.auth.models import User

char_list='abcdefghjkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789-_.!?'

def add(request):
    if request.method == 'POST': # If the form has been submitted...
        form = RfUserForm(request.POST, request.FILES)
        if form.is_valid():
            new_pass = User.objects.make_random_password(length = 10,
                                                    allowed_chars = char_list)
            user = User.objects.create(username = form.cleaned_data['email'],
                                        email = form.cleaned_data['email'],
                                        password = new_pass)
            
            
            user.telefone = form.cleaned_data['telefone']
            user.morada = form.cleaned_data['morada']
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            
            user.save()

            # Redirect after POST
            return HttpResponseRedirect('thanks.html') 
    else:
        form = RfUserForm() # An unbound form

    return render_to_response('add_user.html', {'form': form},
                                context_instance=RequestContext(request))
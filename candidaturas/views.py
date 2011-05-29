from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.template import Template, RequestContext
from candidaturas.models import Candidatura, CandidaturaForm
from django.http import Http404
from utilizadores.models import UserProfile
from utilizadores.views import allowed_chars
from django.contrib.auth.models import User



def detail(request, candidatura_id):
    c = get_object_or_404(Candidatura, pk=candidatura_id)
    return render_to_response('candidaturas/detail.html',
                                    {'candidatura': c})

def add(request):
    if request.method == 'POST': # If the form has been submitted...
        form = CandidaturaForm(request.POST, request.FILES)
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            form.save()
            # Redirect after POST
            return HttpResponseRedirect('candidaturas/thanks.html') 
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
                                                
    user = User.objects.create(username = c.email,
                                    email = c.email,
                                    password = new_pass)
        
        
    user.telefone = c.telefone
    user.morada = c.morada
    user.first_name = c.first_name
    user.last_name = c.last_name
    user.candidatura = c
        
    user.save()
    
    c.aceite = True
    c.save()
    
    return HttpResponseRedirect('/candidaturas/')
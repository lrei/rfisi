from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.template import Template, RequestContext
from django.http import Http404
from utilizadores.models import *
from candidaturas.models import *


def add_medico(request):
    if request.method == 'POST': # If the form has been submitted...
        form = MedicoForm(request.POST, request.FILES)
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            form.save()
            # Redirect after POST
            return HttpResponseRedirect('thanks.html') 
    else:
        form = MedicoForm() # An unbound form

    return render_to_response('add_medico.html', {'form': form},
                                context_instance=RequestContext(request))
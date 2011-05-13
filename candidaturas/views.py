from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.template import Template, RequestContext
from candidaturas.models import Candidatura, CandidaturaForm
from django.http import Http404



def index(request):
    cand_list = Candidatura.objects.all().order_by('-data_candidatura')
    
    return render_to_response('candidaturas/index.html',
                                {'cand_list': cand_list})


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
            return HttpResponseRedirect('/candidaturas/thanks.html') 
    else:
        form = CandidaturaForm() # An unbound form

    return render_to_response('/candidaturas/add.html', {'form': form},
                                context_instance=RequestContext(request))
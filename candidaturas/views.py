from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.template import Template, RequestContext
from candidaturas.models import Candidatura, CandidaturaForm
from django.http import Http404



def detail(request, candidatura_id):
    c = get_object_or_404(Candidatura, pk=candidatura_id)
    return render_to_response('detail.html',
                                    {'candidatura': c})

def add(request):
    if request.method == 'POST': # If the form has been submitted...
        form = CandidaturaForm(request.POST, request.FILES)
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            form.save()
            # Redirect after POST
            return HttpResponseRedirect('thanks.html') 
    else:
        form = CandidaturaForm() # An unbound form

    return render_to_response('add.html', {'form': form},
                                context_instance=RequestContext(request))


def rm(request, candidatura_id):
    c = Candidatura.objects.get(pk=candidatura_id)
    c.delete()
    return HttpResponseRedirect('/candidaturas/')

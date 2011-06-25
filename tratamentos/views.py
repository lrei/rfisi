from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.template import Template, RequestContext, loader, Context
from tratamentos.models import Tratamento, FichaTratamento, FichaForm
from django.http import Http404
from utilizadores.models import UserProfile
from django.contrib.auth.models import User
from datetime import datetime

def tratamentos_list(request):
    tratamentos = Tratamento.objects.all()
    #tratamentos = Tratamento.objects.filter(tratamento__data_fim__isnull=True)
    return render_to_response('tratamentos/tratamentos_list.html',
                                {'tratamentos': tratamentos},
                                context_instance=RequestContext(request))

def detail(request, tratamento_id):
    t = get_object_or_404(Tratamento, pk=tratamento_id)
    fichas = FichaTratamento.objects.filter(tratamento=t)
    if request.method == 'POST': # If the form has been submitted...
        form = FichaForm(request.POST, request.FILES)
        if form.is_valid():
            ficha = FichaTratamento()
            ficha.tratamento = t
            ficha.ficha = form.cleaned_data['ficha']
            ficha.save()
            new_form = FichaForm()
            return render_to_response('tratamentos/detail.html',
                                           {'tratamento': t,
                                           'form': new_form,
                                           'fichas': fichas},
                                    context_instance=RequestContext(request))
               
    form = FichaForm()

    return render_to_response('tratamentos/detail.html', {'tratamento': t,
                                                            'form': form,
                                                            'fichas': fichas},
                                    context_instance=RequestContext(request))

def start(request, paciente_id, fisioterapeuta_id):
    p = User.objects.get(pk=paciente_id)
    f = User.objects.get(pk=fisioterapeuta_id)
    
    tratamento = Tratamento(paciente=p, fisioterapeuta=f)
    tratamento.save()                
 
    return HttpResponseRedirect('/tratamentos/')

def end(request, tratamento_id):
    t = Tratamento.objects.get(pk=tratamento_id)
    
    try:
       t.data_fim = datetime.now()
       t.save()
    except:
        return render_to_response('tratamentos/error.html')

    return render_to_response('tratamentos/detail.html',
                                        {'tratamento': t})

def add(request, tratamento_id):
    t = Tratamento.objects.get(pk=tratamento_id)
    if request.method == 'POST': # If the form has been submitted...
        form = FichaForm(request.POST, request.FILES)
        if form.is_valid():
            ficha = FichaTratamento()
            f.tratamento = t
            f.ficha = form.cleaned_data['ficha']
            f.save()
            return render_to_response('/tratamentos/detail.html',
                                           {'tratamento': t})
               
    else:
        form = FichaForm() # An unbound form
        return render_to_response('tratamentos/add_ficha.html',
                                    {'form': form},
                                    context_instance=RequestContext(request))

    
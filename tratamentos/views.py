from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import Template, RequestContext, loader, Context
from tratamentos.models import Tratamento, FichaTratamento, FichaForm
from django.http import Http404
from utilizadores.models import UserProfile
from django.contrib.auth.models import User
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, mail_admins
from django.conf import settings

@login_required
def tratamentos_list(request):
    if request.user.is_superuser is True:
        currentes =          Tratamento.objects.filter(data_fim__isnull=True).order_by('data_inicio')
        finalizados =         Tratamento.objects.filter(data_fim__isnull=False).order_by('data_inicio')
        return render_to_response('tratamentos/tratamentos_list.html',
                                {'currentes': currentes,
                                'finalizados': finalizados},
                                context_instance=RequestContext(request))
    else:
        tratamentos = Tratamento.objects.filter(fisioterapeuta=request.user)
        currentes =         tratamentos.filter(data_fim__isnull=True).order_by('data_inicio')
        finalizados =         Tratamento.objects.filter(data_fim__isnull=False).order_by('data_inicio')
        return render_to_response('tratamentos/tratamentos_list.html',
                                {'currentes': currentes,
                                'finalizados': finalizados},
                                context_instance=RequestContext(request))

@login_required
def detail(request, tratamento_id):
    t = Tratamento.objects.get(pk=tratamento_id)
    fisio = t.fisioterapeuta
    
    if request.user.is_superuser is False and fisio.id != request.user.id:
            return render_to_response('utilizadores/permerror.html')
    
    
    fichas = FichaTratamento.objects.filter(tratamento=t)
    if request.method == 'POST': # If the form has been submitted...
        form = FichaForm(request.POST, request.FILES)
        if form.is_valid():
            ficha = FichaTratamento()
            ficha.tratamento = t
            ficha.nome = form.cleaned_data['nome']
            ficha.ficha = form.cleaned_data['ficha']
            ficha.save()
            new_form = FichaForm()
            # Send Email Notification to Admins
            notification = "Ficha submetida: " + "http://www." + \
                            settings.MY_SITE_URL + "/tratamentos/" + \
                            str(t.id) +"/"
            mail_admins(settings.MY_SITE_URL + ': Ficha submetida',
                                notification, fail_silently=False)
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
@login_required
def start(request, paciente_id, fisioterapeuta_id):
    
    if request.user.is_superuser is False:
               return render_to_response('utilizadores/permerror.html')
               
    p = User.objects.get(pk=paciente_id)
    f = User.objects.get(pk=fisioterapeuta_id)
    
    t = Tratamento(paciente=p, fisioterapeuta=f)
    t.save()
    
    # Send Email Notification
    notification = "Inicio de tratamento:\n" + "http://www." + \
                    settings.MY_SITE_URL + "/tratamentos/" + str(t.id) + "/"
     
    send_mail(settings.MY_SITE_URL + ': Inicio de tratamento',
                    notification,
                   'do-not-reply@' + settings.MY_SITE_URL,
                   [f.email], fail_silently=False)
 
    return HttpResponseRedirect(reverse('tratamentos'))
    
@login_required
def end(request, tratamento_id):
    t = Tratamento.objects.get(pk=tratamento_id)
    
    #fisio = t.fisioterapeuta
    
    if request.user.is_superuser is False:
            return render_to_response('utilizadores/permerror.html')
    
    if t.data_fim:
        return HttpResponseRedirect(reverse('tratamentos'))
    
    try:
       t.data_fim = datetime.now()
       t.save()
    except:
        return render_to_response('tratamentos/error.html')

    return HttpResponseRedirect(reverse('tratamentos'))


    
from django.shortcuts import render, HttpResponse, redirect


from core.models import Evento


# Create your views here.
def consulta(request,titulo):
    teste = Evento.objects.get(titulo= titulo)
    data = teste.data_evento

    return HttpResponse('<h1> o local é {} data {}</h1>'.format(teste, data))

def lista_eventos(request):
    #evento = Evento.objects.get(id=1)
    evento = Evento.objects.all()
    #usuario = request.user
    #evento = Evento.objects.filter(usuario = usuario)
    dados = {'eventos':evento}
    return render(request,'agenda.html', dados)

#def index(request):
 #   return redirect('agenda/')
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Professor, datashow
from django.views.generic import TemplateView

def registrar(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'usuarios/registrar.html', {'form': form})

def adicionar_professor(request):
    if request.method == 'POST':
        nome = request.POST.get('nome-professor')
        materia = request.POST.get('materia-professor')
        sala = request.POST.get('sala')

        novo_Professor = Professor(nome=nome, sala=sala, materia=materia)
        novo_Professor.save()
        
        return redirect('tabela_professor')
    return render(request, 'adicionar_professor.html')

def tabela_professores(request):
    Professores = Professor.objects.all()
    return render(request, 'tabela_professor.html', {'Professores': Professores})

def remover_professor(request, user_id):
    Professor = get_object_or_404(Professor, id=user_id)
    if request.method == 'POST': 
        Professor.delete()
        return redirect('remover_professor')
    return render(request, 'adicionar_professor.html', {'Professores': Professor.objects.all()})

def adicionar_datashow(request):
    if request.method == 'POST':
        marca = request.POST['marca']
        quantidade = request.POST['quantidade']

        datashow = datashow(marca=marca, quantidade=quantidade)
        datashow.save()

        messages.success(request, 'Data Show adicionado com sucesso!')
        return redirect('adicionar_datashow')

    return render(request, 'usuarios/adicionar_datashow.html')

class AluguelView(TemplateView):
    template_name = 'usuarios/aluguel.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['datashows'] = datashow.objects.all()
        return context

def reservar_datashow(request, datashow_id):
    if request.method == "POST":
        datashow = datashow.objects.get(id=datashow_id)
        datashow.reservado = True
        datashow.save()
        Professores = Professor.objects.all()
        return render(request, 'usuarios/reservar.html', {
            'datashow': datashow,
            'professores': Professores,
            'mensagem': 'Datashow reservado com sucesso. Para qual professor deseja fazer a reserva?'
        })

def confirmar_reserva(request, datashow_id):
    if request.method == "POST":
        Professor_id = request.POST.get('professor_id')
        datashow = datashow.objects.get(id=datashow_id)
        Professor = Professor.objects.get(id=Professor_id)
        datashow.professor = Professor
        datashow.save()
        return redirect('tabela_geral')

class TabelaGeralView(TemplateView):
    template_name = 'usuarios/tabela_geral.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['datashows'] = datashow.objects.filter(reservado=True)
        return context
    
def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

def adicionar(request):
    return render(request, 'adicionar_professor.html')

def logout(request):
    return render(request, 'logout.html')



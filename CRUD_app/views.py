from django.shortcuts import render, redirect
from .forms import InsertFuncionario
from .models import Funcionario


# Create your views here.
def index(request):
    return render(request, 'crud/index.html')


def cria(request):
    if request.method == "POST":
        form = InsertFuncionario(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    form = InsertFuncionario()
    return render(request, 'crud/cadastrar.html', {'form': form})


def listar(request):
    funcionarios = Funcionario.objects.all().order_by('-nome')
    return render(request, 'crud/listar.html', {'funcionarios': funcionarios})


def excluir(request, pk):
    funcionario = Funcionario.objects.get(id=pk)
    funcionario.delete()
    return redirect('listar')


def editar(request, pk):
    funcionario = Funcionario.objects.get(id=pk)
    form = InsertFuncionario(request.POST or None, instance=funcionario)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'crud/editar.html', {'form': form})
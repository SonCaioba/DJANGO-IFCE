from django.shortcuts import render,redirect, get_list_or_404,get_object_or_404
from funcionario.models  import Funcionario
from django.contrib import messages
from funcionario.forms import FuncionarioForm

def AddFuncionario(request):
    template_name = 'funcionario/add_funcionario.html'
    context = {}
    if request.method == 'POST':
        form = FuncionarioForm(request.POST)
        if form.is_valid():
            # f = form.save(commit=False)
            form.save()
            messages.success(request, "Usuário salvo com sucesso!")
        else:
            messages.error(request, "Erro ao salvar dados!")
    form = FuncionarioForm()
    context['form'] = form
    return render(request,template_name,context)



def lista_funcionario(request):
    template_name = 'funcionario/lista_funcionario.html'
    funcionario = Funcionario.objects.all().reverse()
    context = {
       'funcionario':funcionario
    }
    return render(request,template_name,context)
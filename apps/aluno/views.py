from django.shortcuts import render

# Create your views here.
def newAluno(request):
    return render(request,'aluno/add_aluno.html',{})

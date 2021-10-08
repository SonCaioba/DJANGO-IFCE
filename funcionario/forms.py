from django import forms
from funcionario.models import Funcionario


class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        # fields = ['nome','cpf','email','celular','rg','endereco','salario','user',]
        fields = '__all__'

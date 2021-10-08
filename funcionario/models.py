from django.db import models
from django.contrib.auth.models import User

class Funcionario(models.Model):
    nome = models.CharField(max_length=100,help_text='Nome',blank=False)
    cpf = models.CharField(max_length=14,help_text='CPF',blank=False,default='')
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='perfil',default='',blank=False)
    email = models.CharField(max_length=100,help_text='e-mail',default='',blank=False)
    celular = models.CharField(max_length=11,help_text='celular',default='',blank=False)
    rg = models.CharField(max_length=15, help_text='rg', default='',blank=False)
    endereco = models.CharField(max_length=100, help_text='endereco', default='',blank=False)
    salario = models.CharField(max_length=10, help_text='salario', default='',blank=False)

class Meta:
    ordering=['-id']


def __str__(self):
    return self.nome
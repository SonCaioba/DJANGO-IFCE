from django.contrib import admin
from django.urls import include, path



app_name = 'funcionario'

from . import views

urlpatterns = [

    path('',views.AddFuncionario,name='add_funcionario'),
    path('funcionario/lista',views.lista_funcionario,name='lista_funcionario'),

]

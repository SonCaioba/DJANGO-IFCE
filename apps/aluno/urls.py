from django.contrib import admin
from django.urls import include, path
from apps.core import views
app_name = 'aluno'

from . import views
urlpatterns = [
    path('',views.newAluno,name='add_aluno'),

]

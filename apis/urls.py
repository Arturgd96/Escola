from django.urls import path
from .views import *

urlpatterns = [
    path('cursos/', CursoApiView.as_view(), name='cursos'),
    path('alunos/', AlunoApiView.as_view(), name='alunos'),
    path('cursostrilhas/', CursoTrilhaApiView.as_view(), name='cursostrilhas'),
    path('trilhas/', TrilhaApiView.as_view(), name='trilhas'),
    path('turmas/', TurmaApiView.as_view(), name='turmas'),
    path('', Index),
]

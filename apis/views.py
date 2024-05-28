from rest_framework import generics
from .models import *
from .serializers import *
from django.shortcuts import render

def Index(request):
    context = {"dados":'Apis para o curso de Django.'}
    return render(request, 'Index.html', context)


class CursoApiView(generics.ListCreateAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class CursoTrilhaApiView(generics.ListCreateAPIView):
    queryset = CursoTrilha.objects.all()
    serializer_class = CursoTrilhaSerializer


class TrilhaApiView(generics.ListCreateAPIView):
    queryset = Trilha.objects.all()
    serializer_class = TrilhaSerializer


class TurmaApiView(generics.ListCreateAPIView):
    queryset = Turma.objects.all()
    serializer_class = TurmaSerializer


class AlunoApiView(generics.ListCreateAPIView):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

from django.shortcuts import render
from .models import Autor, Post, Comentario
def index(request):
    return render(request, "blog/index.html")
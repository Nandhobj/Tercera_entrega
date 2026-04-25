from .forms import BuscarPostForm
from .models import Post
from django.shortcuts import render
from .models import Autor, Post, Comentario

def index(request):
    return render(request, "blog/index.html")

def about(request):
    return render(request, "blog/about.html")

def buscar_post(request):
    form = BuscarPostForm()
    resultados = None

    if request.GET:
        form = BuscarPostForm(request.GET)
        if form.is_valid():
            titulo = form.cleaned_data.get('titulo')
            resultados = Post.objects.filter(titulo__icontains=titulo)

    return render(request, 'blog/buscar.html', {
        'form': form,
        'resultados': resultados
    })
from django.shortcuts import redirect, get_object_or_404
from .forms import PostForm

def inicio(request):
    return render(request, 'blog/inicio.html')

def crear_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PostForm()

    return render(request, 'blog/crear_post.html', {'form': form})


def lista_posts(request):
    posts = Post.objects.all()
    return render(request, 'blog/lista_posts.html', {'posts': posts})


def detalle_post(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'blog/detalle_post.html', {'post': post})


def editar_post(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('lista_posts')
    else:
        form = PostForm(instance=post)

    return render(request, 'blog/editar_post.html', {'form': form})


def eliminar_post(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == 'POST':
        post.delete()
        return redirect('lista_posts')

    return render(request, 'blog/eliminar_post.html', {'post': post})


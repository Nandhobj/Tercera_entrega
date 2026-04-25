from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path('buscar/', views.buscar_post, name='buscar_post'),
    path('posts/', views.lista_posts, name='lista_posts'),
    path('posts/<int:id>/', views.detalle_post, name='detalle_post'),
    path('crear-post/', views.crear_post, name='crear_post'),
    path('editar-post/<int:id>/', views.editar_post, name='editar_post'),
    path('eliminar-post/<int:id>/', views.eliminar_post, name='eliminar_post'),
    ]


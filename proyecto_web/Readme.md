# Proyecto Django - Blog

## Descripción
Este proyecto corresponde a la tercera entrega del curso de Python en Coderhouse. Se desarrolló una aplicación web utilizando Django con el patrón MVT (Modelo - Vista - Template).

## Funcionalidades

- Página de inicio
- Panel de administración para gestionar datos
- Modelos: Autor, Post y Comentario

## Cómo probar el proyecto

1. Clonar el repositorio
2. Crear y activar entorno virtual
3. Instalar dependencias:
pip install django

4. Ejecutar migraciones:
python manage.py migrate

5. Levantar servidor:
python manage.py runserver

6. Abrir en navegador:
http://127.0.0.1:8000/

## Acceso al panel admin

http://127.0.0.1:8000/admin/

## Estructura del proyecto

- blog: contiene modelos, vistas y templates
- proyecto_web: configuración principal de Django

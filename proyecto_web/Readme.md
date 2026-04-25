# Proyecto Django - Blog / Pages / Mensajería

## Descripción
Aplicación web estilo blog programada en Python con Django (patrón MVT). Incluye autenticación, perfiles, páginas tipo “blog post” con editor enriquecido (CKEditor) y mensajería entre usuarios.

## Rutas principales
- Home: `/`
- About: `/about/`
- Pages (listado): `/pages/`
- Pages (crear): `/pages/create/`
- Mensajes (inbox): `/messages/`
- Admin: `/admin/`
- Login: `/accounts/login/`
- Signup: `/accounts/signup/`
- Profile: `/accounts/profile/`

## Funcionalidades
- Templates con herencia (`blog/base.html`) y NavBar con accesos visibles.
- App `accounts`: registro, login/logout, perfil, edición de perfil, cambio de contraseña.
- App `pages`: CRUD completo con permisos (editar/borrar solo logueado y dueño).
- App `messaging`: inbox/enviados/detalle/compose para mensajes entre usuarios.
- Admin con modelos registrados.

## Cómo correr el proyecto
1. Crear y activar entorno virtual.
2. Instalar dependencias: `pip install -r requirements.txt`
3. Migraciones: `python manage.py migrate`
4. Levantar servidor: `python manage.py runserver`
5. Abrir: `http://127.0.0.1:8000/`

## Nota sobre base de datos / media
- No subir `db.sqlite3` ni `media/` al repo (están en `.gitignore`).

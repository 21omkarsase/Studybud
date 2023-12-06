### Install django

    pip install django

### Create Django Project

    django-admin startproject <project_name>

### Start Django Server

    python manage.py runserver

### Create New App

    python manage.py startapp <app_name>

### Add Template Folder In Base Directory

    settings.py -> templates -> 'DIRS': [
                   BASE_DIR / 'templates'
               ],

### creating templates in app folder

    templates -> base -> home.html
                         room.html

    make changes in views routes
        return render(request, '<app_name>/room.html')

### Applying Default Migrations

    python manage.py migrate

### Create New Migration

    python manage.py makemigrations

### Create admin dashboard user

    python manage.py createsuperuser

# Modal form

    class based representation

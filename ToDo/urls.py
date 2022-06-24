"""ToDo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ToDoList.views import home_view, create_view, edit_view, delete_view, mark_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='To Do'),
    path('create/', create_view, name='Create'),
    path('edit/<int:id>/', edit_view, name='Edit'),
    path('delete/<int:id>/', delete_view, name='Delete'),
     path('mark/<int:id>/', mark_view, name='Mark')
]

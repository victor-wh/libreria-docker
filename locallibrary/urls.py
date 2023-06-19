"""locallibrary URL Configuration

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

from catalog.views import (
    menu,
    AutorList, AutorCreate, AutorUpdate, AutorDelete,
    EditorList, EditorCreate, EditorUpdate, EditorDelete,
    LibroList, LibroCreate, LibroUpdate, LibroDelete)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('menu/', menu, name="menu"),
    # Author
    path('authors/', AutorList.as_view(), name="author_list"),
    path('authors/add/', AutorCreate.as_view(), name="author_add"),
    path('authors/edit/<int:pk>/', AutorUpdate.as_view(), name="author_update"),
    path('authors/delete/<int:pk>/', AutorDelete.as_view(), name="author_delete"),
    # Editor
    path('editor/', EditorList.as_view(), name="editor_list"),
    path('editor/add/', EditorCreate.as_view(), name="editor_add"),
    path('editor/edit/<int:pk>/', EditorUpdate.as_view(), name="editor_update"),
    path('editor/delete/<int:pk>/', EditorDelete.as_view(), name="editor_delete"),
    # Books
    path('books/', LibroList.as_view(), name="book_list"),
    path('books/add/', LibroCreate.as_view(), name="book_add"),
    path('books/edit/<int:pk>/', LibroUpdate.as_view(), name="book_update"),
    path('books/delete/<int:pk>/', LibroDelete.as_view(), name="book_delete"),
]

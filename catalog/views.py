# Django imports
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView,DeleteView

# Local imports
from catalog.forms import AutorForm, EditorForm, LibroForm
from catalog.models import Autor, Editor, Libro


def menu(request):
    return render(request,'menu.html')


# Class based views
class AutorList(ListView):
    model = Autor
    template_name = 'resultados_autores.html'


class AutorCreate(CreateView):
    model = Autor
    form_class = AutorForm
    template_name = 'agregar_autor.html'
    success_url = reverse_lazy('author_list')


class AutorUpdate(UpdateView):
    model = Autor
    form_class = AutorForm
    template_name = 'editar_autor.html'
    success_url = reverse_lazy('author_list')


class AutorDelete(DeleteView):
    model = Autor
    template_name = 'autor_delete.html'
    success_url = reverse_lazy('author_list')


#Editor
class EditorList(ListView):
    model = Editor
    template_name = 'editor_list.html'


class EditorCreate(CreateView):
    model = Editor
    form_class = EditorForm
    template_name = 'editor_form.html'
    success_url = reverse_lazy('editor_list')


class EditorUpdate(UpdateView):
    model = Editor
    form_class = EditorForm
    template_name = 'editor_edit.html'
    success_url=reverse_lazy('editor_list')


class EditorDelete(DeleteView):
    model = Editor
    template_name = 'editor_delete.html'
    success_url = reverse_lazy('editor_list')


#Libros
class LibroList(ListView):
    model = Libro
    template_name = 'libro_list.html'


class LibroCreate(CreateView):
    model = Libro
    form_class = LibroForm
    template_name = 'libro_form.html'
    success_url = reverse_lazy('book_list')


class LibroUpdate(UpdateView):
    model = Libro
    form_class=LibroForm
    template_name = 'libro_edit.html'
    success_url=reverse_lazy('book_list')


class LibroDelete(DeleteView):
    model = Libro
    form_class=LibroForm
    template_name = 'libro_delete.html'
    success_url=reverse_lazy('book_list')

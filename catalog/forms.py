# Django imports
from django import forms

# Local imports
from catalog.models import Autor, Editor, Libro


class AutorForm(forms.ModelForm):

    class Meta:
        model = Autor

        fields = [
            'nombre',
            'apellidos',
            'email',
        ]
        labels ={
            'nombre':'Nombre',
            'apellidos':'Apellidos',
            'email':'Email',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'apellidos':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
        }
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if nombre.lower() == 'abc':
            raise forms.ValidationError("This is not a valid nombre")
        return nombre
class EditorForm(forms.ModelForm):

    class Meta:
        model = Editor

        fields = [
            'nombre',
            'domicilio',
            'ciudad',
            'estado',
            'pais',
            'website',
        ]

        labels = {
            'nombre':'Nombre',
            'domicilio':'Domicilio',
            'ciudad':'Ciudad',
            'estado':'Estado',
            'pais':'Pais',
            'website':'Website',
        }
        widgets = {
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'domicilio':forms.TextInput(attrs={'class':'form-control'}),
            'ciudad':forms.TextInput(attrs={'class':'form-control'}),
            'estado':forms.TextInput(attrs={'class':'form-control'}),
            'pais':forms.TextInput(attrs={'class':'form-control'}),
            'website':forms.TextInput(attrs={'class':'form-control'}),
        }
        
class LibroForm(forms.ModelForm):

    class Meta:
        model = Libro

        fields = [
            'titulo',
            'autores',
            'editor',
            'fecha_publicacion',
        ]
        labels = {
            'titulo':'Titulo',
            'autores':'Autores',
            'editor':'Editor',
            'fecha_publicacion':'Fecha de publicacion',
        }
        widgets = {
            'titulo':forms.TextInput(attrs={'class':'form-control'}),
            'autores':forms.CheckboxSelectMultiple(),
            'editor':forms.Select(attrs={'class':'form-control'}),
            'fecha_publicacion':forms.DateInput(format=('%d/%m/%Y'),attrs={'class':'form-control'}),
        }
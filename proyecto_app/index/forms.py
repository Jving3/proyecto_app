from django import forms
from index.models import Personal


class PersonalForm(forms.ModelForm):
    class Meta:
        imagen = forms.ImageField()
        model = Personal
        fields = ('nombre','telefono', 'cargo', 'imagen')
        labels = {
            'nombre': 'Nombre:',
            'telefono': 'Telefono: ',
            'cargo': 'Cargo: ', 
            'imagen': 'Imagen: ',
        }

class EditarPersonalForm(forms.ModelForm):

    class Meta:
        imagen = forms.ImageField()
        model = Personal
        fields = ('nombre','telefono', 'cargo', 'imagen')
        labels = {
            'nombre': 'Nombre:',
            'telefono': 'Telefono: ',
            'cargo': 'Cargo: ', 
            'imagen': 'Imagen: ',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'id': 'nombre_editar'}),
            'telefono': forms.TextInput(attrs={'id': 'telefono_editar'}),
            'cargo': forms.TextInput(attrs={'id': 'cargo_editar'}),
        }

import datetime
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.forms import TextInput, PasswordInput
from django.http import HttpResponseRedirect
from django.forms import inlineformset_factory
from .models import *

User = get_user_model()


class UserRegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'

    password2 = forms.CharField(label='Confirma Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'ruc', 'cedula', 'tel_cel',
                  'tel_con', 'direccion',
                  'experiencia', 'tipo_persona', 'area_aplica']

        help_texts = {k: "" for k in fields}

        widgets = {

            'username': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'El nombre de usuario puede contener letras, números o caracteres especiales.',
                    'autocomplete': 'off'
                }
            )

        }


class PostForm(forms.ModelForm):
    content = forms.CharField(label='', widget=forms.Textarea(attrs={'rows': 2, 'placeholder': '¿Qué está pasando?'}),
                              required=True)

    class Meta:
        model = Post
        fields = ['content']


class CrearProyectosForm(forms.ModelForm):
    nombre = forms.CharField(label='Nombre Proyecto',
                             widget=forms.Textarea(attrs={'rows': 0, 'placeholder': 'Nombre del proyecto.'}))
    fecha_creacion = forms.DateTimeField(initial=datetime.today)

    class Meta:
        model = Proyectos
        fields = ['nombre', 'direccion', 'relacion_provincia', 'relacion_canton', 'fecha_creacion', 'monto_ref',
                  'numero_viviendas']


class MostrarInvitacionesForm(forms.ModelForm):
    class Meta:
        model = Invitaciones
        fields = ['relacion_usuarioi']


# clase para mostrar el calendario en el forulario ------->


class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'


class CrearAdjudicacionesForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['adjudicado'].queryset = Usuario.objects.none()
        # self.fields['invitacion_ad'].queryset = Invitaciones.objects.none()

    class Meta:
        model = Adjudica
        # adjudicado = forms.ModelChoiceField(queryset=Usuario.objects.all(), widget=forms.Select(attrs={
        #     'class': 'form-control select2'
        # }))
        fields = [
            'invitacion_ad',
            'fecha_adjudica',
            'adjudicado',
            'invitados',

        ]

        labels = {
            'invitacion_ad': 'Invitación',
            'fecha_adjudica': 'Fecha de Adjudicación',
            'adjudicado': 'Adjudicado',
            'invitados': 'Invitados'

        }

        widgets = {
            'invitacion_ad': forms.Select(attrs={'class': 'form-control'}),
            'fecha_adjudica': DateTimeInput(attrs={'class': 'form-control'}),
            # 'adjudicado': forms.Select(attrs={'class': 'form-control'}),
            'adjudicado': forms.Select(attrs={'class': 'form-control'}),
            'invitados': forms.Select(attrs={'class': 'form-control'}),

        }


class CrearInvitacionesForm(forms.ModelForm):
    class Meta:
        model = Invitaciones
        fields = [
            'relacion_usuarioi',
            'relacion_procesoi',
        ]
        widgets = {
            'fecha_invitacion': forms.DateInput(attrs={
                'class': 'form-control', 'value': datetime.now().strftime('%Y-%m-%d')
            }, format='%Y-%m-%d'),
            'relacion_usuarioi': forms.Select(attrs={'class': 'form-control'}),
            'relacion_procesoi': forms.Select(attrs={'class': 'form-control'}),

        }

class InvitacionesForm(forms.Form):
    procesos = forms.ModelChoiceField(widget=forms.Select(attrs={
        'class': 'form-control'
    }), queryset=Proceso.objects.all(), label='Proceso')


class CrearInvitadosForm(forms.ModelForm):
    model = Invitados
    exclude = ()


ChildFormset = inlineformset_factory(
    Invitaciones,
    Invitados,
    form=CrearInvitadosForm,
    fields=('invitado',),
    extra=4,
    fk_name='invitaciones',
    widgets={
        'invitado': forms.Select(attrs={'class': 'form-control'}),
        'fecha': DateTimeInput(attrs={'class': 'form-control', 'value': datetime.now().strftime('%Y-%m-%d')},
                               format='%Y-%m-%d'),
        'relacion_usuarioi': forms.Select(attrs={'class': 'form-control'}),
    }
)

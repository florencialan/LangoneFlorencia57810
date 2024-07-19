from django import forms
from .models import Capacitaciones, Asesorias, Gestiones, Soluciones  # Importa todos los modelos
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CapacitacionesForm(forms.ModelForm):
    cliente = forms.CharField(max_length=50, required=True, label="Nombre de tu empresa")
    tematica = forms.CharField(required=True)
    
    class Meta:
        model = Capacitaciones  # Ahora Capacitaciones está importado y definido correctamente
        fields = '__all__'  # O especifica los campos que deseas incluir en el formulario
        
class AsesoriasForm(forms.ModelForm):
    cliente = forms.CharField(max_length=60, required=True, label="Nombre de tu empresa")
    tematica = forms.CharField(required=True)
    correo_corporativo = forms.EmailField(required=True)
    
  
    class Meta:
        model = Asesorias  # Ahora Capacitaciones está importado y definido correctamente
        fields = '__all__'  # O especifica los campos que deseas incluir en el formulario
        
class GestionesForm(forms.ModelForm):
    cliente = forms.CharField(max_length=50, required=True, label="Nombre de tu empresa")
    correo_corporativo = forms.EmailField(required=True)
    
    
    class Meta:
        model = Gestiones  # Ahora Capacitaciones está importado y definido correctamente
        fields = '__all__'  # O especifica los campos que deseas incluir en el formulario

class SolucionesForm(forms.ModelForm):
    cliente = forms.CharField(max_length=50, required=True, label="Nombre de tu empresa")
    fecha_inicio_de_servicio = forms.DateField(required=True)
    solucionado = forms.BooleanField(required=True)
    
    
    class Meta:
        model = Soluciones  # Ahora Capacitaciones está importado y definido correctamente
        fields = '__all__'  # O especifica los campos que deseas incluir en el formulario


class RegistroForm(UserCreationForm):
    correo = forms.EmailField(required=True)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Contraseña a confirmar", widget=forms.PasswordInput)
    

    class Meta:
        model = User
        fields = ["username", "correo", "password1", "password2"]
        

class UserEditForm(UserChangeForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(label="Nombre", max_length=50, required=True)
    last_name = forms.CharField(label="Apellido", max_length=50, required=True)
    
    class Meta:
        model = User
        fields = ["email", "first_name", "last_name"]
        
class AvatarForm(forms.Form):
    imagen = forms.ImageField(required=True)
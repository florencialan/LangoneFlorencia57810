from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Capacitaciones, Asesorias, Gestiones, Soluciones, Avatar
from .forms import CapacitacionesForm, AsesoriasForm, GestionesForm, SolucionesForm , RegistroForm, UserEditForm , UserChangeForm, User, AvatarForm

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import  AuthenticationForm
from django.contrib.auth.views import  PasswordChangeView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required



# Copyright Florencia Langone

def home(request):
    return render(request, "entidades/index.html")

def acerca(request):
    return render(request, "entidades/acerca.html")

# Capacitaciones

@login_required
def capacitaciones(request):
    contexto = {"capacitaciones": Capacitaciones.objects.all()}
    return render(request, "entidades/capacitaciones.html", contexto)


@login_required
def capacitacionesForm(request):
    if request.method == "POST":
        miForm = CapacitacionesForm(request.POST)
        if miForm.is_valid():
            capacitaciones_cliente = miForm.cleaned_data.get("cliente")
            capacitaciones_tematica = miForm.cleaned_data.get("tematica")
            capacitaciones = Capacitaciones(cliente=capacitaciones_cliente, tematica=capacitaciones_tematica)
            capacitaciones.save()
            contexto = {"capacitaciones": Capacitaciones.objects.all()}
            return render(request, "entidades/capacitaciones.html", contexto)
    else:
        miForm = CapacitacionesForm()
    return render(request, "entidades/capacitacionesForm.html", {"form": miForm})

@login_required
def buscarCapacitaciones(request):
    return render(request, "entidades/buscar.html")

@login_required
def encontrarCapacitaciones(request):
    if 'buscar' in request.GET:
        patron = request.GET['buscar']
        capacitaciones = Capacitaciones.objects.filter(tematica__icontains=patron)
        contexto = {'capacitaciones': capacitaciones}
    else:
        contexto = {'capacitaciones': Capacitaciones.objects.all()}
    return render(request, "entidades/capacitaciones.html", contexto)

@login_required
def capacitacionesUpdate(request, id_capacitaciones):
    capacitaciones = Capacitaciones.objects.get(id=id_capacitaciones)
    if request.method == "POST":
        miForm = CapacitacionesForm(request.POST, instance=capacitaciones)
        if miForm.is_valid():
            miForm.save()
            contexto = {"capacitaciones": Capacitaciones.objects.all()}
            return render(request, "entidades/capacitaciones.html", contexto)
    else:
        miForm = CapacitacionesForm(instance=capacitaciones)
    return render(request, "entidades/capacitacionesForm.html", {"form": miForm})

@login_required
def capacitacionesDelete(request, id_capacitaciones):
    capacitaciones = Capacitaciones.objects.get(id=id_capacitaciones)
    capacitaciones.delete()
    contexto = {"capacitaciones": Capacitaciones.objects.all()}
    return render(request, "entidades/capacitaciones.html", contexto)


# Asesorias

class AsesoriaListView(LoginRequiredMixin, ListView):
    model = Asesorias
    template_name = 'entidades/asesorias_list.html'  # Asegúrate de tener esta plantilla

class AsesoriaCreateView(LoginRequiredMixin, CreateView):
    model = Asesorias
    form_class = AsesoriasForm
    template_name = 'entidades/asesoriasForm.html'
    success_url = reverse_lazy('asesorias')  # Ajusta el nombre según tu configuración

class AsesoriaUpdateView(LoginRequiredMixin, UpdateView):
    model = Asesorias
    form_class = AsesoriasForm
    template_name = 'entidades/asesoriasForm.html'
    success_url = reverse_lazy('asesorias')  # Ajusta el nombre según tu configuración

class AsesoriaDeleteView(LoginRequiredMixin, DeleteView):
    model = Asesorias
    template_name = 'entidades/asesorias_confirm_delete.html'
    success_url = reverse_lazy('asesorias')  # Ajusta el nombre según tu configuración


# Gestiones

@login_required
def gestiones(request):
    contexto = {"gestiones": Gestiones.objects.all()}
    return render(request, "entidades/gestiones.html", contexto)


@login_required
def gestionesForm(request):
    if request.method == "POST":
        miForm = GestionesForm(request.POST)
        if miForm.is_valid():
            miForm.save()
            contexto = {"gestiones": Gestiones.objects.all()}
            return render(request, "entidades/gestiones.html", contexto)
    else:
        miForm = GestionesForm()
    return render(request, "entidades/gestionesForm.html", {"form": miForm})

@login_required
def gestionesUpdate(request, id_gestiones):
    gestiones = Gestiones.objects.get(id=id_gestiones)
    if request.method == "POST":
        miForm = GestionesForm(request.POST, instance=gestiones)
        if miForm.is_valid():
            miForm.save()
            contexto = {"gestiones": Gestiones.objects.all()}
            return render(request, "entidades/gestiones.html", contexto)
    else:
        miForm = GestionesForm(instance=gestiones)
    return render(request, "entidades/gestionesForm.html", {"form": miForm})

@login_required
def gestionesDelete(request, id_gestiones):
    gestiones = Gestiones.objects.get(id=id_gestiones)
    gestiones.delete()
    contexto = {"gestiones": Gestiones.objects.all()}
    return render(request, "entidades/gestiones.html", contexto)


# Soluciones

@login_required
def soluciones(request):
    contexto = {"soluciones": Soluciones.objects.all()}
    return render(request, "entidades/soluciones.html", contexto)

def solucionesForm(request):
    if request.method == "POST":
        miForm = SolucionesForm(request.POST)
        if miForm.is_valid():
            miForm.save()
            contexto = {"soluciones": Soluciones.objects.all()}
            return render(request, "entidades/soluciones.html", contexto)
    else:
        miForm = SolucionesForm()
    return render(request, "entidades/solucionesForm.html", {"form": miForm})


#________Login / Logout / Registration

def loginRequest(request):
    if request.method  == "POST":
        usuario = request.POST["username"]
        clave = request.POST["password"]
        user = authenticate(request, username=usuario, password=clave)
        if user is not None:
            login(request, user)
            
            
            #__________________________Buscar Avatar
            try:
                avatar = Avatar.objects.get(user=request.user.id).imagen.url
            except:
                avatar = "/media/avatares/default.png"
            finally:
                request.session["avatar"] = avatar
            
            #_____________________________________________________________
            return redirect(reverse_lazy("home"))
           # return render(request, "entidades/index.html")
        else:
            return redirect(reverse_lazy('login'))
                     
    else:
        miForm = AuthenticationForm()
        
        
    return render(request, "entidades/login.html", {"form": miForm})


def register(request):
    if request.method  == "POST":
        miForm = RegistroForm(request.POST)
        if miForm.is_valid():
           usuario = miForm.cleaned_data.get("username")
           miForm.save()
           return redirect(reverse_lazy('home'))
                     
    else:
        miForm = RegistroForm()
        
        
    return render(request, "entidades/registro.html", {"form": miForm})

#_________Edicion de perfil / Avatar

@login_required
def editProfile(request):
    usuario = request.user
    if request.method == "POST":
        miForm = UserEditForm(request.POST)
        if miForm.is_valid():
            user = User.objects.get(username=usuario)
            user.email = miForm.cleaned_data.get("email")
            user.first_name = miForm.cleaned_data.get("first_name")
            user.last_name = miForm.cleaned_data.get("last_name")
            user.save()
            return redirect(reverse_lazy("home"))


    else:
        miForm = UserEditForm(instance=usuario)
    return render(request, "entidades/editarPerfil.html", {"form": miForm})


class CambiarClave(LoginRequiredMixin, PasswordChangeView):
    template_name = "entidades/password.html"
    success_url = reverse_lazy("home")
   
@login_required
def agregarAvatar(request):
    if request.method == "POST":
        miForm = AvatarForm(request.POST, request.FILES)
        if miForm.is_valid():
            usuario = User.objects.get(username=request.user)
            imagen = miForm.cleaned_data["imagen"]
          #borrar avatares viejos
            avatarViejo = Avatar.objects.filter(user=usuario)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()
            #__________________________________________
          
            avatar = Avatar(user=usuario, imagen=imagen)
            avatar.save()
            
            #____________________Enviar la imagen al home
            imagen = Avatar.objects.get(user=usuario).imagen.url
            request.session["avatar"] = imagen
            #___________________________________________________
            return redirect(reverse_lazy("home"))


    else:
        miForm = AvatarForm()
    return render(request, "entidades/agregarAvatar.html", {"form": miForm})

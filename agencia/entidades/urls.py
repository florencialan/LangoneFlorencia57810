from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('acerca/', acerca, name="acerca"),
    
    # Capacitaciones
    path('capacitaciones/', capacitaciones, name="capacitaciones"),
    path('capacitacionesForm/', capacitacionesForm, name="capacitacionesForm"),
    path('buscarCapacitaciones/', buscarCapacitaciones, name="buscarCapacitaciones"),
    path('encontrarCapacitaciones/', encontrarCapacitaciones, name="encontrarCapacitaciones"),
    path('capacitacionesUpdate/<int:id_capacitaciones>/', capacitacionesUpdate, name="capacitacionesUpdate"),
    path('capacitacionesDelete/<int:id_capacitaciones>/', capacitacionesDelete, name="capacitacionesDelete"),
    
    # Asesorias
    path('asesorias/', AsesoriaListView.as_view(), name="asesorias"),
    path('asesoriasCreate/', AsesoriaCreateView.as_view(), name="asesoriasCreate"),
    path('asesoriasUpdate/<int:pk>/', AsesoriaUpdateView.as_view(), name="asesoriasUpdate"),
    path('asesoriasDelete/<int:pk>/', AsesoriaDeleteView.as_view(), name="asesoriasDelete"),
    
    # Gestiones
    path('gestiones/', gestiones, name="gestiones"),
    path('gestionesForm/', gestionesForm, name="gestionesForm"),
    path('gestionesUpdate/<int:id_gestiones>/', gestionesUpdate, name="gestionesUpdate"),
    path('gestionesDelete/<int:id_gestiones>/', gestionesDelete, name="gestionesDelete"),
    
    # Soluciones
    path('soluciones/', soluciones, name="soluciones"),
    path('solucionesForm/', solucionesForm, name="solucionesForm"),
    
    # Login/Logout/Registracion
    path('login/', loginRequest, name="login"),
    path('logout/', LogoutView.as_view(template_name="entidades/logout.html"), name="logout"),
    path('registro/', register, name="registro"),
    
    # Edicion de perfil / Avatar
    path('perfil/', editProfile, name="perfil"),
    path('agregar_avatar/', agregarAvatar, name="agregarAvatar"),
    
    # Ruta para cambiar la clave
    path('<int:pk>/password/', CambiarClave.as_view(), name="password"),
    
]



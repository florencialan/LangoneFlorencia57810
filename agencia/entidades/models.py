from django.db import models
from django.contrib.auth.models import User

# Modelo de negocio de la aplicación.

class Capacitaciones(models.Model):
    # Representa una capacitación ofrecida a un cliente.
    cliente = models.CharField(max_length=50)  # Nombre del cliente.
    tematica = models.CharField(max_length=60, default="")  # Tema de la capacitación.
    
    class Meta:
        verbose_name = "Capacitación"  # Nombre en singular para el panel de administración.
        verbose_name_plural = "Capacitaciones"  # Nombre en plural para el panel de administración.
        ordering = ["id"]  # Ordena los registros por el campo 'id'.
    
    def __str__(self):
        # Devuelve una representación legible del objeto.
        return f"{self.cliente}, {self.tematica}"
    
class Asesorias(models.Model):
    # Representa una asesoría ofrecida a un cliente.
    cliente = models.CharField(max_length=60)  # Nombre del cliente.
    tematica = models.CharField(max_length=60)  # Tema de la asesoría.
    correo_corporativo = models.EmailField()  # Correo electrónico corporativo del cliente.
    
    class Meta:
        verbose_name = "Asesoría"  # Nombre en singular para el panel de administración.
        verbose_name_plural = "Asesorías"  # Nombre en plural para el panel de administración.
    
    def __str__(self):
        # Devuelve una representación legible del objeto.
        return f"{self.tematica}, {self.cliente}"
    
class Gestiones(models.Model):
    # Representa una gestión o interacción con un cliente.
    cliente = models.CharField(max_length=50)  # Nombre del cliente.
    correo_corporativo = models.EmailField()  # Correo electrónico corporativo del cliente.
    
    class Meta:
        verbose_name = "Gestión"  # Nombre en singular para el panel de administración.
        verbose_name_plural = "Gestiones"  # Nombre en plural para el panel de administración.
        ordering = ["cliente", "correo_corporativo"]  # Ordena los registros por 'cliente' y luego por 'correo_corporativo'.
    
    def __str__(self):
        # Devuelve una representación legible del objeto.
        return f"{self.correo_corporativo}, {self.cliente}"
    
class Soluciones(models.Model):
    # Representa una solución proporcionada a un cliente.
    cliente = models.CharField(max_length=50)  # Nombre del cliente.
    fecha_inicio_de_servicio = models.DateField()  # Fecha en la que comenzó el servicio.
    solucionado = models.BooleanField()  # Indica si la solución ha sido proporcionada (True) o no (False).
    
    class Meta:
        verbose_name = "Solución"  # Nombre en singular para el panel de administración.
        verbose_name_plural = "Soluciones"  # Nombre en plural para el panel de administración.
        
    def __str__(self):
        # Devuelve una representación legible del objeto.
        return f"{self.solucionado}, {self.cliente}"
    
class Avatar(models.Model):
    # Representa un avatar asociado a un usuario.
    imagen = models.ImageField(upload_to="avatares")  # Imagen del avatar que se sube al directorio 'avatares'.
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Relación con el modelo User de Django.
    
    def __str__(self):
        # Devuelve una representación legible del objeto.
        return f"{self.user}, {self.imagen}"

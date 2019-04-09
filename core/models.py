from django.db import models

# Create your models here.
class Usuario(models.Model):
    alias = models.CharField(max_length=15, verbose_name = "Usuario")
    nombre = models.CharField(max_length=30, verbose_name = "Nombres")
    apellido = models.CharField(max_length=30,verbose_name = "Apellidos")
    correo = models.EmailField(verbose_name = "Correo")
    password = models.CharField(max_length=30, verbose_name = "Contraseña")
    fecha_registro = models.DateField(auto_now_add=True, verbose_name="Fecha de Registro")    
    foto = models.ImageField(verbose_name = "Foto de Perfil", upload_to="usuario")

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ["-fecha_registro"]
    
    # Servira para mostrar en el admin
    def __str__(self):
        return self.alias

class Post(models.Model):
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)    
    descripcion = models.TextField(verbose_name="Descripción")
    likes = models.IntegerField(verbose_name="Likes")
    ubicacion = models.TextField(verbose_name="Coordenadas")
    fecha_post = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Posteo")
    foto = models.ImageField(verbose_name="Captura", upload_to="post")

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ["-fecha_post"]

    def __str__(self):
        return self.descripcion

class Puesto(models.Model):
    usuario = models.ManyToManyField(Usuario)
    nombre = models.CharField(max_length=30,verbose_name='Nombre del Puesto')
    dias_atencion = models.CharField(max_length=30, name="Dias de Atención")
    hora_apertura = models.TimeField(verbose_name="Hora de apertura")
    hora_cierre = models.TimeField(verbose_name="Hora de Cierre")
    descripcion = models.TextField(verbose_name='Descripción')
    puntuacion = models.IntegerField(verbose_name='Puntuación')
    ubicacion = models.TextField(verbose_name="Coordenadas")
    foto = models.ImageField(verbose_name='Foto',upload_to="puesto") 

class Plato(models.Model):
    puesto = models.ForeignKey(Puesto,on_delete=models.CASCADE)
    nombre = models.CharField(max_length=30, verbose_name="Nombre del Plato")
    precio = models.FloatField(verbose_name="Precio")
    descripcion = models.TextField(verbose_name="Descripción del Plato")
    foto = models.ImageField(verbose_name="Foto", upload_to="plato")

class Comentario(models.Model):    
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    puesto = models.ForeignKey(Puesto, on_delete=models.CASCADE)
    texto = models.TextField(verbose_name="Comentario")    
    fecha = models.DateTimeField(auto_now_add=True,verbose_name="Fecha y Hora")
    
    class Meta:
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentario'
        ordering = ["-fecha"]

    def __str__(self):
        return "Comentario"

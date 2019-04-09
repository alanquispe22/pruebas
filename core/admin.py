from django.contrib import admin
from .models import Usuario,Puesto, Comentario, Plato, Post

# Register your models here.
class UsuarioAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_registro','correo')

class PuestoAdmin(admin.ModelAdmin):
    readonly_fields = ('puntuacion')

class ComentarioAdmin(admin.ModelAdmin):
    readonly_fields = ('texto','fecha')

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('likes')

admin.site.register(Post)
admin.site.register(Plato)
admin.site.register(Comentario)
admin.site.register(Usuario)
admin.site.register(Puesto)
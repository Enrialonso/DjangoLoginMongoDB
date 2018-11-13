from django.contrib import admin
from .models import Usuario
# Register your models here.

# Creamos esta clase para que en el panel de adminitracion puedan aparecer los campos
# de solo lectura por ejemplo el de creacion de un usuario y el de modificacion

class UsuarioAdmin(admin.ModelAdmin):
    readonly_fields = ('creado', 'actualizado')

# Damos de alta el modelo de base de datos creado para que 
# pueda ser visible en el panel de administracion, tambien le pasamos la 
# clase anterior para que muestra los campos que son de  solo lectura
admin.site.register(Usuario, UsuarioAdmin)
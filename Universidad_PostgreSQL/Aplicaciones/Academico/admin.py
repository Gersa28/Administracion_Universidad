from django.contrib import admin
from .models import Curso
from .models import Docente
# Register your models here.

@admin.register(Curso) #Esta es ota forma de regitrar por eso comenté #admin.site.register(Curso,CursoAdmin)
class CursoAdmin(admin.ModelAdmin):
    list_display=('id','coloreado','credits', 'docente')
    ordering = ('id', 'nombre','credits')
    search_fields = ('id','nombre','credits')
    #list_editable = ('nombre','credits')
    list_display_links = ('coloreado',)
    list_filter = ('credits',)
    # list_per_page = 3 #Paginación

    #exclude = ('credits',) 
    #no me deja editar los créditos, ni añadirlos con un nuevo curso
    # (al no tener un valor por defecto(default) me dará un error)

    """    
    fieldsets = (
        (None,{
            'fields':('nombre',)
        }),
        ('Advances options',{
            'classes':('collapse','wide','extrapretty'),
            'fields':('credits',)
        })
    )
    """

    def datos(self,obj):
        return obj.nombre.upper()
    
    datos.short_description = "CURSO (MAYÚSCULAS)"
    datos.empty_value_display = "???"
    datos.admin_order_field = 'nombre'

    
    admin.site.register(Docente)
#admin.site.register(Curso,CursoAdmin)
from django.urls import path

from Aplicaciones.Academico.views import CursoListView
from Aplicaciones.Academico.views import eliminar_curso
from Aplicaciones.Academico.views import registrar_curso
from Aplicaciones.Academico.views import edicion_curso
from Aplicaciones.Academico.views import editar_curso, contacto

urlpatterns = [
    path('', CursoListView.as_view(), name='gestion_cursos'),
    path('eliminacionCurso/<int:id>', eliminar_curso),
    path('registrarCurso/', registrar_curso),
    path('edicionCurso/<int:id>', edicion_curso),
    path('editarCurso/', editar_curso),
    path('contacto/', contacto)
]

import os
os.system('cls')

# python manage.py shell
# from django.db import models
# from Aplicaciones.Academico.models import Curso 

# cur = Curso.objects.create(nombre = 'Tecnología',credits = 2) #Agrega datos
# cursos = Curso.objects.all()
# print(cursos)
# Para ver la tabla por consola:
# cursos = Curso.objects.all()
# exec("for c in cursos: print('{0}: {1} - {2}'.format(c.id,c.nombre,c.credits))")
# cursoEditar = Curso.objects.get(id=2)
# cursoEditar.nombre = 'Probabilidad y estadísticas'
# cursoEditar.credits = 8
# cursoEditar.save()
# cursoEliminar = Curso.objects.get(id=1)
# cursoEliminar.delete()


# def home(request):
#     cursosListados=Curso.objects.all()
    
#     return render(request, "gestionCursos.html", {"cursos": cursosListados})
#     # enviamos cursosLIstados a gestionCursos.html a través de Render, al cual 
#     # se podrá acceder con el Alias "cursos"
    
#     #return HttpResponse("<h1>Hola Mundo!</h1>")

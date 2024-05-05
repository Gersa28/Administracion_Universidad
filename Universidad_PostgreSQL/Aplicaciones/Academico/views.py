from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.http import HttpResponse
from .models import Curso


# Create your views here.

# VISTA BASADA EN FUNCIONES:
# def home(request):
    # cursosListados = Curso.objects.all().order_by('nombre','credits')
   # cursosListados = Curso.objects.all()[:5]
    # cursosListados2=Curso.objects.all()[4:5]
    # cursosListados3=Curso.objects.all()[6:]
    # cursosListados4=Curso.objects.all().order_by('nombre')
    # cursosFiltrado=Curso.objects.all().order_by('nombre','credits')
    # cursosListados5=Curso.objects.all().order_by('-nombre') #Orden descendente
    # si se repiten nombres se ordena por el segundo parámetro
    # cursosFiltrado = Curso.objects.all().order_by('nombre', 'credits')
    # cursosFiltrado1 = Curso.objects.filter(nombre='BIOINGENIERÍA I')
    # cursosFiltrado2 = Curso.objects.filter(
    #     nombre='BIOINGENIERÍA I', credits='4')
    # cursosFiltrado3 = Curso.objects.filter(
    #     credits__gte=4)  # mayores o iguales a 4
    # cursosFiltrado3 = Curso.objects.filter(
    #     credits__lte=4)  # menores o iguales a 4
    # cursosFiltrado4 = Curso.objects.filter(nombre__startswith='M')
    # cursosFiltrado5 = Curso.objects.filter(nombre__contains='G')

    # data = {
    #     'titulo': 'Gestion de Cursos',
    #     'cursos': cursosListados,
    # }

    # return render(request, "gestionCursos.html", data)

    # return render(request, "gestionCursos.html", {"cursos": cursosFiltrado})
    # enviamos cursosLIstados a gestionCursos.html a través de Render, al cual
    # se podrá acceder con el Alias "cursos"

#VISTA BASADA EN CLASES (MODELOS):
class CursoListView(ListView):
    model = Curso
    template_name= 'gestionCursos.html'

    def get_queryset(self):
        #return Curso.objects.filter(credits__lte=4) #Se muestran solo los resultados filtrador
        return Curso.objects.all().order_by('nombre','credits')
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['titulo'] = 'Gestión de Cursos'
        # print(context)
        return context 

def eliminar_curso(request,id):
    curso=Curso.objects.get(id=id)
    curso.delete()
    return redirect('/') # Redirigir a la ruta raíz

def registrar_curso(request):
    nombre=request.POST['txtNombre']
    credits=request.POST['numCreditos']
    curso=Curso.objects.create(nombre=nombre, credits=credits)
    return redirect('/')

def edicion_curso(request, id):
    curso=Curso.objects.get(id=id)
    data = {
        'titulo': 'Edición de Curso',
        'curso': curso
    }
    return render(request, "edicionCurso.html", data)

def editar_curso(request):
    id = int(request.POST['id'])

    nombre=request.POST['txtNombre']
    credits=request.POST['numCreditos']

    curso=Curso.objects.get(id=id)
    curso.nombre=nombre
    curso.credits=credits
    curso.save()
    return redirect('/')

def contacto(request):
    return render(request, "contacto.html")

    
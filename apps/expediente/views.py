from django.shortcuts import render,redirect
from django.http import HttpResponse
from apps.expediente.formulariosLaboratorio.formulario_resultado_labo import FormResultLab #desde la carpeta apps/expediente/formulariosLaboratorio.formulario_resultado_labo importar la clase FormResultLab
#formulariosLaboratorio es una carpeta que contiene todos los formularios del area de laboratorio
from apps.expediente.models import ResultadoExamen #importando modelo
from django.views.generic import ListView,CreateView,TemplateView #importando clases para las vistas 
from django.core.urlresolvers import reverse_lazy #importando la funcion para redirigir
# Create your views here.

#Nota: {'clave',contexto}: sentencia de un diccionario

def index(request):
	#return HttpResponse("index")
	return render(request,'expediente/registro_respuesta_examen.html')

'''def ver_form_registro_result_labo(request):# esta funcion permite ingresar los resultados de la evaluacion de laboratorio
		if request.method == 'POST':
		form = FormResultLab(request.POST)
		if form.is_valid():
			form.save()
		return redirect('expediente:index')#redirigiendo a la pagina index. El namespace se encuentra en el archivo urls.py de la carpeta raiz para identificar las vistas correspondientes a la interfaz del area de laboratorio
	else: 
		form = FormResultLab()
	return render(request, 'expediente/registro_respuesta_examen.html',{'form':form})# agregando desde la carpeta templates/expediente/registro_respuesta_examen.html y enviando el contexto
'''
#listar
class ver_listado_reg_result_lab(ListView):
	model = ResultadoExamen
	template_name = 'expediente/listado_registros_resultados_labo.html'#indicando la plantilla a utilizar

#registro
class ver_form_registro_registro_labo(CreateView):
	model = ResultadoExamen
	form_class = FormResultLab #indicando el formulario a utilizar
	template_name= 'expediente/registro_respuesta_examen.html'#indicando el tipo de plantilla para el formulario
	#redirigiendo con un url resolver a la vista listar registros de resultado de laboratorio mediante su namespace
	success_url = reverse_lazy('expediente:list_reg_lab')

#buscar
class buscar_reg_result_lab(TemplateView):

	def post(self, request, *args, **kwargs):
		buscar = request.POST['Busqueda'] #obteniendo el valor del campo de busqueda del formulario contenido en la plantilla listado_registros_resultados_labo.html
		ResultExam = ResultadoExamen.objects.filter(Expediente__numeroArchivo=buscar)#filtrando los datos mediante una FK
		return render(request, 'expediente/buscar_reg_result_lab.html',{'encontrado':ResultExam})#enviando los resultados a el template buscar_reg_result_lab.html
		

		
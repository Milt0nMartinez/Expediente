from django.conf.urls import url,include
#from apps.expediente.views import index,ver_form_registro_result_labo,ver_listado_reg_result_lab \ ver_listado_reg_result_lab #importando vistas
from apps.expediente.views import index,ver_listado_reg_result_lab,ver_form_registro_registro_labo, buscar_reg_result_lab #importando vistas


urlpatterns = [
    url(r'^$',index),#referenciando a la funcion de vista index del archivo views.py de la apps expediente
    url(r'^registro$',ver_form_registro_registro_labo.as_view(), name='reg_result_lab'),#referenciando a la clase de vista ver_form_registro_result_labo del archivo views.py de la apps expediente
    url(r'^listar$',ver_listado_reg_result_lab.as_view(), name='list_reg_lab'),#referenciando a la clase de vista ver_listado_reg_result_lab del archivo views.py de la apps expediente
    url(r'^buscar$',buscar_reg_result_lab.as_view(template_name='expediente/buscar_reg_result_lab.html'),name='buscar_reg_lab'),#referenciando a la clase de vista buscar_reg_result_lab del archivo views.py de la apps expediente
    #NOTA: a la vista de tipo TemplateView no se puede referenciar sin darle un nombre de plantilla que sera la que se encuentra en la carpeta correspondiente de plantillas de la aplicacion
]

#para acceder a la vista desde el navegador:
#localhost:8000/url del archivo de urls de la app contenida entre los caracteres ^$
from django.template import Template, Context, loader
from django.http import HttpResponse
import datetime
from aplicacion.models import *
from random import randint



def bienvenida(request):
    return HttpResponse("Bienvenidos a la clase de Django")

def bienvenida_html(request):
    hoy = datetime.datetime.now()
    response = f"""
    <html>
    <h1>Bienvenidos a la clase de Django</h1>
    <h2>Esta es la comision 55630</h2>
    <h3>hoy es {hoy} </h3>
    """
    return HttpResponse(response)

def saludar(request, nombre):
    response = f"Hola, bienvenido {nombre} a la clase de Django!!"
    return HttpResponse(response)


def calcular_bruto(request, neto):
    neto = int(neto)
    response = f"<html><h1>El bruto de la factura es {neto*1.21} $</h1></html>"
    return HttpResponse(response)


def saludar2(request, nombre, apellido):
    response = f"Hola, bienvenido {nombre} {apellido} a la clase de Django!!"
    return HttpResponse(response)

def clase18(request):
    nombre = "Pablo"
    apellido = "Onetto"
    curso = "Python y Django"
    notas = [5, 3, 7, 9, 8]
    diccionario = {"nombre": nombre, "apellido": apellido, "curso": curso, "notas": notas}
    
    plantilla = loader.get_template('clase18.html')
    
    
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)

def agregar_curso(request):
    nro_comision = randint(1,999999)
    str_nombre = "Python"
    curso = Curso(nombre=str_nombre, comision=nro_comision)
    curso.save()
    documento = f"<htlm><h1>Se acaba de crear el curso de {str_nombre} para la comisión {nro_comision}</h1></htlm>"
    return HttpResponse(documento)
   


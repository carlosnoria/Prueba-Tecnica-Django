"""
Prueba Tecnica Kronos
Autor: Carlos Noria

Los modelos se diseñaron de modo que cumpliera con las especificaciones 
y fuesen de manipulacion eficiente.

Se evito la creacion de un modelo relacional intermedio para cumplir
de una manera mas sencilla y eficiente con los requerimientos.

Se considero que la clase 'Ciudad' bastaba con que tuviese nombre y 
una clave primaria autoincremental 'id'.

La clase 'Usuario' posee los 3 datos fundamentales para representar a una
persona como lo son el nombre, el apellido y el documento de identidad
siendo este unico poseedor de una restriccion de unicidad. Para de esta
manera recrear un poco lo que ocurre en el mundo real.

La clase 'Tienda' posee el nombre, la ciudad en la que se encuentra
y los usuarios que pertenecen a dicha 'Tienda', siendo el campo 'users' 
poseedor de una relacion 'ManyToManyField' para cumplir con el 
requerimiento de la prueba, se decidio colocar la relacion en la 
tabla 'Tienda' porque es mas natural y en este caso mas eficiente 
trabajar bajo la premisa de que una 'Tienda' tiene varios suscriptores en 
lugar de trabajar bajo la premisa de que un 'Usuario' esta suscrito
a varias tiendas.

No se incluyo ningun tipo de seguridad sobre esta API pues todos los metodos
o endpoints son unicamente de acceso de datos sin posibilidad de modificacion
ni eliminacion.
"""

from django.db import models

class Ciudad(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        ordering = ["name"]

class Usuario(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    document = models.CharField(max_length=10, unique=True)

class Tienda(models.Model):
    name = models.CharField(max_length=30)
    city = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    users = models.ManyToManyField(Usuario)

    class Meta:
        ordering = ["city", "name"]

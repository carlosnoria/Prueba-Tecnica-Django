"""
Prueba Tecnica Kronos
Autor: Carlos Noria
"""

from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include('kronos_rest.urls')),
]
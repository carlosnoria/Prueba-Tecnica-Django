"""
Prueba Tecnica Kronos
Autor: Carlos Noria

Se decidio Utilizar vistas basadas en clases porque hacen a la 
API REST mas facil de mantener y de comprender.
"""
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from rest_framework import generics, mixins
from kronos_rest.models import Ciudad, Tienda, Usuario
from kronos_rest.serializers import CiudadSerializer, TiendaSerializer, UsuarioSerializer

""" 
Vista del endpoint GET para obtener todos los usuarios de una tienda
"""
class user_list_by_shop(generics.ListAPIView):
    serializer_class = UsuarioSerializer
    lookup_field = "pk"

    def get_queryset(self):
        pk = self.kwargs.get(self.lookup_field)
        try:
            shop = Tienda.objects.get(id=pk)
            return shop.users

        except Tienda.DoesNotExist:
            raise Http404

"""
Vista del endpoint GET para obtener todos las tiendas a las que esta asociado un usuario
"""
class shop_list_by_user(generics.ListAPIView):
    serializer_class = TiendaSerializer
    lookup_url_kwarg = "pk"

    def get_queryset(self):
        pk = self.kwargs.get(self.lookup_url_kwarg)
        shops = Tienda.objects.filter(users__id=pk)
        if not shops:
            raise Http404
        else:
            return shops


"""
Vista del endpoint GET para obtener las tiendas de una ciudad a las que esta asociado un
usuario.
"""
class shop_list_from_city_by_user(generics.ListAPIView):
    serializer_class = TiendaSerializer
    lookup_url_kwarg = 'city_id'
    slug_field = 'userPk'

    def get_queryset(self):
        cityId = self.kwargs.get(self.lookup_url_kwarg)
        userId = self.kwargs.get(self.slug_field)
        shops = Tienda.objects.filter(city_id=cityId).filter(users__id=userId)
        if not shops:
            raise Http404
        else:
            return shops
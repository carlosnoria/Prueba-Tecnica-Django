from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from rest_framework import generics, mixins
from kronos_rest.models import Ciudad, Tienda, Usuario
from kronos_rest.serializers import CiudadSerializer, TiendaSerializer, UsuarioSerializer

class user_list_by_shop(mixins.RetrieveModelMixin, generics.GenericAPIView):
    serializer_class = UsuarioSerializer
    lookup_field = "pk"

    def get_queryset(self):
        pk = self.kwargs.get(self.lookup_field)
        try:
            shop = Tienda.objects.get(id=pk)
            return shop.users

        except Tienda.DoesNotExist:
            raise Http404
        
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class shop_list_by_user(mixins.RetrieveModelMixin, generics.GenericAPIView):
    serializer_class = TiendaSerializer
    lookup_url_kwarg = "pk"

    def get_queryset(self):
        pk = self.kwargs.get(self.lookup_url_kwarg)
        shops = Tienda.objects.filter(users__id=pk)
        return shops

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

class shop_list_from_city_by_user(mixins.RetrieveModelMixin, generics.GenericAPIView):
    serializer_class = TiendaSerializer
    lookup_field = 'city_id'
    slug_field = 'userPk'

    def get_queryset(self):
        cityId = self.kwargs.get(self.lookup_field)
        userId = self.kwargs.get(self.slug_field)
        shops = Tienda.objects.filter(city_id=cityId).filter(users__id=userId)
        return shops

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
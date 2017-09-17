from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from kronos_rest.models import Ciudad, Tienda, Usuario
from kronos_rest.serializers import CiudadSerializer, TiendaSerializer, UsuarioSerializer

@api_view(['GET'])
def user_list_by_shop(request, pk):
    try:
        shop = Tienda.objects.get(id=pk)

    except Tienda.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        users = shop.users
        serializer = UsuarioSerializer(users, many=True)
        return Response(serializer.data)

    else:
        pass

@api_view(['GET'])
def shop_list_by_user(request, pk):
    try:
       user = Usuario.objects.get(id=pk)

    except Usuario.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET': 
        shops = Tienda.objects.filter(users__id=pk)
        serializer = TiendaSerializer(shops, many=True)
        return Response(serializer.data)

    else:
        pass

@api_view(['GET'])
def shop_list_from_city_by_user(request, cityPk, userPk):
    try:
        city = Ciudad.objects.get(id=cityPk)
        user = Usuario.objects.get(id=userPk)

    except (Ciudad.DoesNotExist, Usuario.DoesNotExist):
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        shops = Tienda.objects.filter(city_id=cityPk).filter(users__id=userPk)
        serializer = TiendaSerializer(shops, many=True)
        return Response(serializer.data)

    else:
        pass
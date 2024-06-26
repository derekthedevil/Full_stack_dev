from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializers
from rest_framework.decorators import api_view ,permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework_api_key.models import APIKey
from rest_framework_api_key.permissions import HasAPIKey
from rest_framework.authentication import TokenAuthentication
from django.views.decorators.csrf import csrf_exempt

@api_view(["GET","POST"])
# @permission_classes([HasAPIKey])
def drink_list(request):
    if request.method == "GET" :
        drinks  = Drink.objects.all()
        serializers =DrinkSerializers(drinks,many=True)
        return JsonResponse({"drinks" :serializers.data})
    if request.method == "POST":
        serializer = DrinkSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)


@api_view(['GET','PUT','DELETE'])
@csrf_exempt
def drink_detail(request,id):
    try:
        drink = Drink.objects.get(pk=id)
    except Drink.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = DrinkSerializers(drink)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = DrinkSerializers(drink,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method =="DELETE":
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# my-remote-service 50sA0mfr.cUpLGkCwpUtN4DtFNbQygK564ID9YP8h

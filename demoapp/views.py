from django.shortcuts import render
from .serializers import UserSerializer
from .models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework.request import Request
from rest_framework.response import Response
from .permissions import IsAdminOrReadOnly
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework import generics


def index(request):
    return render(request, "templates/index.html")


"""
Generics
"""


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all().order_by("pk")
    serializer_class = UserSerializer
    permission_classes = []


class UserList(generics.ListAPIView):
    queryset = User.objects.all().order_by("pk")
    serializer_class = UserSerializer
    permission_classes = []


class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all().order_by("pk")
    serializer_class = UserSerializer
    permission_classes = []


class UserUpdate(generics.UpdateAPIView):
    queryset = User.objects.all().order_by("pk")
    serializer_class = UserSerializer
    permission_classes = []
    lookup_field = "pk"


class UserDelete(generics.DestroyAPIView):
    queryset = User.objects.all().order_by("pk")
    serializer_class = UserSerializer
    permission_classes = []
    lookup_field = "pk"


"""
Class Based View: ApiView
"""
# class UserList(APIView):
#     permission_classes = [IsAdminOrReadOnly]

#     def get(self, request: Request, *args, **kwargs):
#         query = User.objects.all()
#         serializers = UserSerializer(query, many=True)
#         return Response(serializers.data, status=status.HTTP_200_OK)

#     def post(self, request: Request, *args, **kwargs):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class UserDetail(APIView):
#     permission_classes = [IsAdminOrReadOnly]

#     def get(self, request: Request, pk: int, *args, **kwargs):
#         query = User.objects.get(id=pk)
#         serializer = UserSerializer(query)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def put(self, request: Request, pk: int):
#         query = User.objects.get(id=pk)
#         serializer = UserSerializer(query, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)sd

#     def delete(self, request: Request, pk: int):
#         query = User.objects.get(id=pk)
#         query.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


"""
Function Based View
"""
# @api_view(http_method_names=["GET", "POST"])
# @permission_classes([permissions.IsAuthenticatedOrReadOnly])
# def UserView(request: Request):
#     query = User.objects.all()

#     if request.method == "POST":
#         """
#         To send data through DjangoRestFramework
#         data = {
#             "firstname": request.data.get("firstname"),
#             "lastname": request.data.get("lastname"),
#         }
#         """

#         # Pass data through PostMan
#         data = request.data

#         serializer = UserSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     serializer = UserSerializer(query, many=True)
#     return Response(serializer.data, status=status.HTTP_200_OK)


# @api_view(["GET"])
# def SingleBill(request: Request, bill_idx: int):
#     if request.method == "GET":
#         query = User.objects.all()[bill_idx - 1]
#         serializer = UserSerializer(query)
#         return Response(serializer.data, status=status.HTTP_200_OK)

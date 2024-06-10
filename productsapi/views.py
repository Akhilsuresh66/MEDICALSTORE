from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from rest_framework.authtoken.models import Token
from rest_framework import status
from med_acc.models import Medicine 
from med_acc.forms import MedicineForm
from .serializers import MedicineSerializer
from django.shortcuts import get_object_or_404

#signup api
@api_view(['POST'])
@permission_classes((AllowAny,))
def signup(request):
    form = UserCreationForm(data=request.data)
    if form.is_valid():
        user = form.save()
        return Response("Account created successfully", status=status.HTTP_201_CREATED)
    return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)


#login api
@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},status=HTTP_200_OK)


#create api
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_Medicine(request):
    form = MedicineForm(request.POST)
    if form.is_valid():
        Medicine = form.save()
        return Response({'id': Medicine.id}, status=status.HTTP_201_CREATED)
    return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)

#read 
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_Medicine(request):
    Medicines= Medicine.objects.all()
    serializer = MedicineSerializer(Medicines, many=True)
    return Response(serializer.data)


#update
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_Medicine(request, pk):
    medicines = get_object_or_404(Medicine, pk=pk)
    form = MedicineForm(request.data, instance=medicines)
    if form.is_valid():
        form.save()
        serializer = MedicineSerializer(medicines)
        return Response(serializer.data)
    else:
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
    
#delete
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_Medicine(request, pk):
    try:
        Medicines = Medicine.objects.get(pk=pk)
    except Medicine.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    Medicines.delete()
    return Response("Deleted successfully")

#search
@api_view(['GET'])
@permission_classes((AllowAny,))
def searchmedicine_api(request):
    query = request.GET.get('query', '')
    medicines = Medicine.objects.filter(name__istartswith=query)
    serializer = MedicineSerializer(medicines, many=True)
    return Response(serializer.data)
from rest_framework import generics
from .serializers import FridgeSerializer
from .models import Fridge
from django.http import JsonResponse

# Create your views here.
def fridge_list(request):
    fridges = Fridge.objects.all().values('fridge_name', 'image_url')
    fridges_list = list(fridges)
    return JsonResponse(fridges_list, safe=False)

class FridgeList(generics.ListCreateAPIView):
    queryset = Fridge.objects.all()
    serializer_class = FridgeSerializer

class FridgeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Fridge.objects.all()
    serializer_class = FridgeSerializer

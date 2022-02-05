from rest_framework import generics
from .models import Jogos
from .serializers import JogosSerialiazers


# Create your views here.
class JogosCreatAPIView(generics.ListCreateAPIView):
        queryset = Jogos.objects.all()
        serializer_class = JogosSerialiazers
        
        
class JogosDetailAPIView(generics.RetrieveAPIView):        
        queryset = Jogos.objects.all()
        serializer_class = JogosSerialiazers 
        lookup_field = 'id'
        

class JogosListAPIView(generics.ListAPIView):
        queryset = Jogos.objects.all()
        serializer_class = JogosSerialiazers
        
        
class JogosDeleteAPIView(generics.DestroyAPIView, generics.RetrieveAPIView):
        queryset = Jogos.objects.all()
        serializer_class = JogosSerialiazers 
        lookup_field = 'id'
        

class JogosUpdateAPIView(generics.UpdateAPIView, generics.ListAPIView):
        queryset = Jogos.objects.all()
        serializer_class = JogosSerialiazers 
        lookup_field = 'id'
      
        
class JogosDeleteAllApiView(generics.DestroyAPIView, generics.ListAPIView):
        queryset = Jogos.objects.all()
        serializer_class = JogosSerialiazers 
        

from .serializers import LinkSerializer
from .models import Links
from rest_framework import generics, status
from rest_framework.response import Response



# Create your views here.
class PostListApi(generics.ListAPIView):
    queryset=Links.objects.filter(active=True)
    serializer_class = LinkSerializer

 
class PostCreateApi(generics.CreateAPIView):
    queryset = Links.objects.filter(active=True)
    serializer_class = LinkSerializer

 
class PostDetailApi(generics.RetrieveAPIView):
    queryset = Links.objects.filter(active=True)
    serializer_class = LinkSerializer


class PostUpdateApi(generics.UpdateAPIView): 
    queryset = Links.objects.filter(active=True)
    serializer_class = LinkSerializer
 

class PostDeleteApi(generics.DestroyAPIView):
    queryset= Links.objects.filter(active=True)
    serializer_class = LinkSerializer


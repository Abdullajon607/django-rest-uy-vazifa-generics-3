from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Test
from .serializers import TestSerializer

class TestApiViews(ListCreateAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

class TestDetailApiViews(RetrieveUpdateDestroyAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
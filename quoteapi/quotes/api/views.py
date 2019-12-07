from rest_framework import generics, permissions
from rest_framework.generics import get_object_or_404

from quotes.models import Quote
from quotes.api.serializers import QuoteSerializer
from quotes.api.permissions import IsAdminUserOrReadOnly
from quotes.api.pagination import SmallSetPagination

class QuoteListCreateAPIView(generics.ListCreateAPIView):
    
    queryset = Quote.objects.all().order_by("-id") # pagination 사용시 쿼리셋의 order가 정의되어야함
    serializer_class = QuoteSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    pagination_class = SmallSetPagination
    
class QuoteDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quote.objects.all().order_by("-id")
    serializer_class = QuoteSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    
    

    
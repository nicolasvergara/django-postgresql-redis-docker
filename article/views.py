from pyexpat import model
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework import filters

from article import serializers
from article import models

"""
class ArticleViewSet(viewsets.ViewSet):
    queryset = models.Article.objects.all()
    serializer_class = serializers.ArticleSerializer

    @method_decorator(cache_page(60*60*2))
    def retrieve(self, request, pk=None):
        article = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(article)
        return Response(serializer.data)
"""
class PostPagination(PageNumberPagination):
    page_size = 1

class ArticleViewSet(ListAPIView):
    queryset = models.Article.objects.all().order_by('-date_added')
    serializer_class = serializers.ArticleSerializer
    pagination_class = PostPagination
    filter_backends = [filters.SearchFilter,]
    search_fields = ['author', 'title', 'description',]
    ordering_fields = ['price', 'date_added',]

    @method_decorator(cache_page(60*2))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
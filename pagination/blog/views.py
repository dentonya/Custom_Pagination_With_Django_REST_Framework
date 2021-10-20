from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from .models import Post
from .serializers import PostSerializer


# Create your views here.
def index(request):
    return render(request, 'blog/index.html')

# Create Pagination class how many post
class PostPagination(PageNumberPagination):
    page_size = 3

class PostViewSet(viewsets.ModelViewSet):
    pagination_class = PostPagination
    serializer_class = PostSerializer
    queryset = Post.objects.all()

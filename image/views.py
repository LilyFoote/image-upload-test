# Create your views here.

from rest_framework.generics import CreateAPIView
from rest_framework import parsers

from .models import Image
from .serializers import ImageSerializer


class ImageView(CreateAPIView):
    model = Image
    serializer_class = ImageSerializer
    parser_classes = (parsers.MultiPartParser,)

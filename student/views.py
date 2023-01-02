from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import studentSerializer
from .models import stud

# Create your views here.


@api_view(['GET'])
def navigation(request):
    api_urls = {
        'student-list': '/student-list/',
    }
    return Response(api_urls)


@api_view(['GET'])
def studentList(request):
    students = stud.objects.all()
    serializer = studentSerializer(students, many=True)
    return Response(serializer.data)

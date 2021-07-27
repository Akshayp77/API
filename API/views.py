import json
import re
from API.models import Emp
from re import S
from rest_framework import serializers
from API.serializer import EmpSerializer
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.decorators import api_view


# Create your views here.
def details(request):
    return HttpResponse("Employees Data")

class api(APIView):

    def get(self,request):
        x=Emp.objects.all()
        serializer=EmpSerializer(x,many=True)
        j_d= JSONRenderer().render(serializer.data)
        return HttpResponse(j_d,content_type='application/json')
    
    @csrf_exempt
    def post(self,request):
        name=request.POST['nm']
        e_id=request.POST['id']
        salary=request.POST['sal']
        Emp.objects.create(name=name,e_id=int(e_id),salary=int(salary))
        return HttpResponse("Data Entered")
    #@api_view(['PUT',])
    def put(self,request):
        #import pdb; pdb.set_trace()
        data=request.data
        p=data['id']
        name=data['nm']
        e_id=data['e_id']
        salary=data['sal']
        x=Emp.objects.get(pk=p)
        x.name= name
        x.e_id= int(e_id)
        x.salary=int(salary)
        x.save()
        return HttpResponse("Data Updated")
    def delete(self,request): 
        data=request.data
        p=data['id']
        x=Emp.objects.get(pk=p)
        x.delete()
        return HttpResponse("Data deleted Successfully")
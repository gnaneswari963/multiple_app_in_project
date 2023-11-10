from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def rohith(request):
    return render(request,'rohith.html')

def rohith1(request):
    return HttpResponse('Rohith is a indian cricketer')
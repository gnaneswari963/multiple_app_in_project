from django.shortcuts import render 
from django.http import HttpResponse

# Create your views here.
def dhoni(request):
    return render(request,'dhoni.html')

def dhoni1(request):
    return HttpResponse('Dhoni is a indian cricketer')
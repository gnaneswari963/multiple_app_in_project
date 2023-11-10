from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def virat(request):
    return render(request,'virat.html')

def virat1(request):
    return HttpResponse('virat is a indian cricketer')
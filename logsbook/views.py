from django.shortcuts import render, HttpResponse

# Create your views here.

def logs(request):
    return HttpResponse("i am a boy")

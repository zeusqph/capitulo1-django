from django.shortcuts import render,HttpResponse

def index(requerst):
    return HttpResponse("Hello,world.You're at the polls index.")
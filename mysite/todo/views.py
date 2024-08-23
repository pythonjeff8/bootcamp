#from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


# Create your views here.

def index(request):
    return HttpResponse("<h1>Todo!</h1>")

#     Function methond vs class object method
# def about(request):
#    return HttpResponse("This is the about page")

class AboutView(View):
    def get(self, request):
        return HttpResponse("This is the about page")
    

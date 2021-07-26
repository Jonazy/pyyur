from django.shortcuts import render, redirect
from django.contrib import messages


# Create your views here.

# Landing page function
def home(request):
    template_name = 'index.html'
    if request.method == 'GET':
        context = {

        }
        return render(request, template_name, context)

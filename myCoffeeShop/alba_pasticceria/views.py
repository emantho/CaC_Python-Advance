from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from . import forms
import datetime

# Create your views here.

# def index(request):
#     return HttpResponse("Hello to ALBA PASTICCERIA")

def index(request):
    
    my_context_var = {
        'userName':'Diana',
        'dateTime': datetime.datetime.now()
    }
    
    return render(request, 'alba_pasticceria/index.html', my_context_var)

def sayHello(request, userName):
    return HttpResponse(("Hello World {} from Django, Welcome ".format(userName)))

def listName(request):
    
    my_context = {
        'names' : [
            "Paola Moreno",
            "Laura Fernandez",
            "Emilia Manjarres"
        ], 
        'payment_status': True
        
    }
    
    return render(request, 'alba_pasticceria/nameList.html', my_context)

def abm_users(request):
    
    # Controlling request flow 
    
    context = {}
    
    if request == 'GET':
        context['abm_users_form'] = forms.AbmUserForm()
    
    else: # Asummig is a POST
        context['abm_users_form'] = forms.AbmUserForm(request.POST)
    
        # Form validation
        # If correct, inform with message and redirect 

        # IF NO correct 
        # Saty in form but showing an error
        # return redirect('index')
        
    return render(request, 'alba_pasticceria/abm_users.html', context)
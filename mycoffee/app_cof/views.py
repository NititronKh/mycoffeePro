from django.shortcuts import render
from django.http.response import HttpResponse
from datetime import datetime
from .models import Coffee



def coffees(request):
    all_coffees = Coffee.objects.order_by('-is_premium')
    context = {"coffees" : all_coffees}
    return render(request,"app_cof/coffees.html",context)

def coffee(request,coffee_id):
    one_coffee = None
    try:
        one_coffee = Coffee.objects.get(id=coffee_id)
    except:
        print("ไม่พบเมนูนี้")
    context = {"coffee":one_coffee}
    return render(request,"app_cof/coffee.html",context)

# Create your views here.

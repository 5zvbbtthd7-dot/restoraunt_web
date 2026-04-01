from django.shortcuts import render, get_object_or_404, redirect
from .models import Dish

def home(request):
    dishes = Dish.objects.all()[:6]
    return render(request, 'home.html', {'dishes': dishes})

def menu(request):
    dishes = Dish.objects.all()
    return render(request, 'menu.html', {'dishes': dishes})

def dish_detail(request, id):
    dish = get_object_or_404(Dish, id=id)
    return render(request, 'dish.html', {'dish': dish})
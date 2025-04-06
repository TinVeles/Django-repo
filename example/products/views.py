from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm, RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

# Create your views here.
def kras(request):
    return render(request, 'kras/index.html')

def stolbi (request):
    return render (request, 'kras/stolbi_kras.html')

def home(request):
    items = Item.objects.all()
    return render(request, 'products/home.html', {'items': items})

@login_required
def add_item(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.owner = request.user
            item.save()
            return redirect('home')
    else:
        form = ItemForm()
    return render(request, 'products/add_item.html', {'form': form})

@login_required
def edit_item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ItemForm(instance=item)
    return render(request, 'products/edit_item.html', {'form': form})

@login_required
def delete_item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == "POST":
        item.delete()
        return redirect('home')
    return render(request, 'products/delete_item.html', {'item': item})

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})
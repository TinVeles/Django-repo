from django import forms
from .models import Item
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description', 'category']
        labels = {
            "name": "Имя",
            "description": "Описание",
            "category": "Категория",
            
        }

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

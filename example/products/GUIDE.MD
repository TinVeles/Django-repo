# Как работает Django между urls.py, views.py, models.py и forms.py

# Общая схема взаимодействия компонентов
Браузер (запрос)
   ↓
urls.py  — определяет, какой view вызвать
   ↓
views.py — получает данные, обрабатывает логику
   ↓
models.py — взаимодействует с базой данных
forms.py  — создаёт и обрабатывает формы
   ↓
templates/ — HTML-страница, которую видит пользователь



## 1. `urls.py` — маршруты (роутинг)

Файл `urls.py` определяет, какую функцию во `views.py` вызывать при переходе по определенному URL.

**Пример:**

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),            # /
    path('add/', views.add_item, name='add_item') # /add/
]
```

## 2. `views.py` — логика отображения и обработки

`views.py` — это "мозг страницы", здесь:
- выбираются данные из базы (через модели)
- создаются формы (из `forms.py`)
- вызывается нужный HTML-шаблон

**Пример:**

```python
from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm

def home(request):
    items = Item.objects.all()
    return render(request, 'products/home.html', {'items': items})

def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ItemForm()
    return render(request, 'products/add_item.html', {'form': form})
```

## 3. `models.py` — работа с базой данных

Здесь описываются таблицы базы данных через Python-классы.

**Пример:**

```python
from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
```

## 4. `forms.py` — формы и валидация данных

Формы используются для сбора, отображения и проверки данных, которые вводит пользователь.

**Пример:**

```python
from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description']
        labels = {
            "name": "Имя",
            "description": "Описание",
        }
```

## Пример полной цепочки: добавление элемента

**1. Пользователь открывает `/add/`**

- В `urls.py` вызывается `views.add_item`.

**2. `views.py` решает:**
- если `GET`: отдать пустую форму
- если `POST`: принять данные формы и сохранить в базу

**3. `forms.py` обрабатывает форму**
- Проверяет, все ли поля заполнены
- Если да — создаёт `Item` в базе

**4. `models.py` взаимодействует с таблицей `Item`**

**5. Отдаётся HTML-шаблон `add_item.html` с формой**

## Вывод

| Файл        | Роль                                            |
|-------------|-------------------------------------------------|
| `urls.py`   | Связывает URL с функцией во `views.py`          |
| `views.py`  | Обрабатывает запросы, передаёт данные в шаблон  |
| `models.py` | Работает с базой данных (ORM)                   |
| `forms.py`  | Отображает и проверяет формы                    |









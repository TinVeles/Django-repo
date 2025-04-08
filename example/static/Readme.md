# Инструкция по подключению статических файлов в Django

## 1. Измените настройки в файле settings.py

В файле settings.py убедитесь, что у вас указаны следующие настройки:

```python
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    BASE_DIR / 'static',
)
```

## 2. Подключение статических файлов в HTML

В HTML-шаблоне подключите статику следующим образом:

```html
{% load static %}
<link href="{% static 'styles/css/index.css' %}" rel="stylesheet">
```

## 3. Запуск сервера

После внесения всех изменений запустите сервер командой:

```bash
python manage.py runserver
```

Теперь статические файлы должны корректно подключаться и отображаться.

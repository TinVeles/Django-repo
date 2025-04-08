# Как настроить pytest для Django

Этот документ описывает базовые шаги по установке и настройке pytest для проекта на Django.

## Шаг 1: Установка зависимостей

Установите `pytest` и плагин `pytest-django`, выполнив команду:

```bash
pip install pytest pytest-django
```

```bash
uv add pytest pytest-django
```

## Шаг 2: Создание файла конфигурации pytest

Создайте в корневой директории проекта файл `pytest.ini` со следующим содержимым:

```ini
[pytest]
DJANGO_SETTINGS_MODULE = your_project.settings
python_files = tests.py test_*.py *_tests.py
```

Замените `your_project.settings` на путь к вашим настройкам Django.

## Шаг 3: Написание тестов

Создайте файлы тестов (например, `test_views.py`, `test_models.py`) и напишите тесты, используя синтаксис pytest. Пример:

```python
import pytest
from django.urls import reverse

@pytest.mark.django_db
def test_home_view(client):
    url = reverse('home')
    response = client.get(url)
    assert response.status_code == 200
```

## Шаг 4: Запуск тестов

Запустите тесты, выполнив в терминале команду:

```bash
pytest -v 
```

Pytest автоматически обнаружит файлы с тестами и выполнит их.
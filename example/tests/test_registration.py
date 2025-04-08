import pytest
from django.urls import reverse
from django.contrib.auth.models import User

@pytest.mark.django_db
def test_register_page_loads(client):
    """
    Проверка, что страница регистрации загружается и использует правильный шаблон.
    """
    url = reverse('register')
    response = client.get(url)
    assert response.status_code == 200, "Страница регистрации недоступна"
    templates = [t.name for t in response.templates if t.name is not None]
    assert 'registration/register.html' in templates, "Не используется шаблон регистрации"

@pytest.mark.django_db
def test_register_user(client):
    """
    Проверка успешной регистрации нового пользователя.
    """
    url = reverse('register')
    data = {
        'username': 'newuser',
        'email': 'newuser@example.com',
        'password1': 'VeryStrongPass123',
        'password2': 'VeryStrongPass123'
    }
    response = client.post(url, data)
    assert response.status_code == 302, "После регистрации не произошло перенаправление"
    assert User.objects.filter(username='newuser').exists(), "Пользователь не создан"

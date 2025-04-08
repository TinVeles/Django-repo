import pytest
from django.urls import reverse

@pytest.mark.django_db
def test_home_page_accessible(client):
    """
    Проверка доступности главной страницы.
    """
    url = reverse('home')
    response = client.get(url)
    assert response.status_code == 200, "Главная страница недоступна"

@pytest.mark.django_db
def test_kras_page_accessible(client):
    """
    Проверка доступности страницы 'Красноярск'.
    """
    url = reverse('kras')
    response = client.get(url)
    assert response.status_code == 200, "Страница 'kras' недоступна"

@pytest.mark.django_db
def test_stolbiki_page_accessible(client):
    """
    Проверка доступности страницы 'столбики'.
    """
    url = reverse('stolb')
    response = client.get(url)
    assert response.status_code == 200, "Страница 'stolbiki' недоступна"

@pytest.mark.django_db
def test_add_item_requires_authentication(client):
    """
    Проверка, что доступ к добавлению элемента требует авторизации.
    Неавторизованный пользователь должен быть перенаправлен на страницу логина.
    """
    url = reverse('add_item')
    response = client.get(url)
    # Обычно редирект означает 302. В Django клиент перенаправляет на /accounts/login/?next=...
    assert response.status_code == 302, "Неавторизованный пользователь получил доступ к add_item"
    
@pytest.mark.django_db
def test_add_item_authenticated(client, test_user):
    client.login(username='testuser', password='testpass123')
    url = reverse('add_item')
    response = client.get(url)
    assert response.status_code == 200


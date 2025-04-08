import pytest
from django.contrib.auth.models import User

@pytest.fixture
def test_user(db):
    """
    Фикстура, создающая тестового пользователя.
    """
    user = User.objects.create_user(username='testuser', password='testpass123')
    return user

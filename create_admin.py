import os
import django
from django.contrib.auth import get_user_model

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CarMatch.settings')
django.setup()

User = get_user_model()

username = 'admin'
email = 'admin@example.com'
password = 'admin123'

try:
    user = User.objects.get(username=username)
    print(f"Суперпользователь уже существует: {user.username}")
    print(f" - is_active: {user.is_active}")
    print(f" - is_staff: {user.is_staff}")
    print(f" - is_superuser: {user.is_superuser}")
except User.DoesNotExist:
    print(f"Создание суперпользователя {username}...")
    User.objects.create_superuser(username=username, email=email, password=password)
    print(f"Суперпользователь {username} создан.") 
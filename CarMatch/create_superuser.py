import os
import django
from django.contrib.auth import get_user_model

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CarMatch.settings')
django.setup()

User = get_user_model()

username = 'admin'
email = 'admin@example.com'
password = 'admin123'

if not User.objects.filter(username=username).exists():
    print(f'Создание суперпользователя {username}...')
    User.objects.create_superuser(username, email, password)
    print(f'Суперпользователь {username} создан.')
else:
    print(f'Суперпользователь {username} уже существует.') 
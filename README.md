# 🎬 Кинотеатр — Бронирование билетов (Backend)

Бэкенд REST API для дипломного проекта «Сайт-агрегатор просмотра и бронирования билетов». Обеспечивает управление фильмами, залами, сеансами, бронированием и генерацию QR-кодов.

---

## 📌 Стек технологий

- **Язык:** Python 3.11
- **Фреймворк:** Django 5.2 + Django REST Framework (DRF)
- **База данных:** PostgreSQL
- **Аутентификация:** JWT (через `djangorestframework-simplejwt`)
- **Дополнительно:** `psycopg2-binary` (драйвер БД), `Pillow` (работа с изображениями), `qrcode` (генерация QR-кодов)
- **Веб-сервер:** Встроенный сервер Django (для разработки)

---

## 📂 Структура проекта
movie-booking-backend/
├── bookings/ # Приложение для бронирований
│ ├── models.py # Модели: Booking (связь сеанс-место-пользователь)
│ ├── views.py # API для создания и просмотра броней
│ ├── serializers.py # Сериализатор для модели Booking
│ └── admin.py # Регистрация модели в админке Django
├── config/ # Основная конфигурация Django
│ ├── settings.py # Настройки проекта (БД, приложения, JWT и т.д.)
│ └── urls.py # Корневые маршруты API
├── halls/ # Приложение для залов и мест
│ ├── models.py # Модели: Hall (зал), Seat (место в зале)
│ ├── views.py # API для управления залами и местами
│ ├── serializers.py # Сериализаторы для Hall и Seat
│ └── admin.py
├── movies/ # Приложение для фильмов
│ ├── models.py # Модель: Movie (фильм)
│ ├── views.py # API для списка и деталей фильмов
│ ├── serializers.py # Сериализатор для Movie
│ └── admin.py
├── shows/ # Приложение для сеансов
│ ├── models.py # Модель: Session (сеанс фильма в зале)
│ ├── views.py # API для управления сеансами и списка мест
│ ├── serializers.py # Сериализатор для Session
│ └── admin.py
├── users/ # Приложение для пользователей
│ ├── models.py # Кастомная модель User с полем role (admin/user)
│ ├── views.py # API для регистрации, входа (JWT) и списка пользователей
│ ├── serializers.py
│ └── admin.py
├── media/ # Папка для загруженных пользователем файлов
│ └── qr_codes/ # Сгенерированные QR-коды для билетов
├── requirements.txt # Список всех необходимых Python-пакетов
├── manage.py # Управляющий скрипт Django
└── README.md # Документация проекта

text

---

## 🚀 Инструкция по развёртыванию и запуску (локально)

### Шаг 1: Клонирование репозитория
```bash
git clone https://github.com/Gala-knd/movie-booking-backend.git
cd movie-booking-backend

---

### Шаг 2: Создание и активация виртуального окружения

**Для Windows (Git Bash):**

```bash
python -m venv venv
source venv/Scripts/activate
```

---

**Для Mac / Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### Шаг 3: Установка зависимостей

```bash
pip install -r requirements.txt
```

---

### Шаг 4: Настройка базы данных PostgreSQL

Убедитесь, что PostgreSQL установлен и запущен.

**Создайте базу данных:**

```sql
CREATE DATABASE movie_booking_db;
```

**В файле `config/settings.py` укажите свои данные:**

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'movie_booking_db',
        'USER': 'postgres',
        'PASSWORD': 'ваш_пароль',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

---

### Шаг 5: Применение миграций и создание суперпользователя

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

---

### Шаг 6: Запуск сервера

```bash
python manage.py runserver
```

Сервер будет доступен по адресу:

```text
http://127.0.0.1:8000/
```

---

# 🌐 API Эндпоинты

| Метод | Эндпоинт | Описание |
|--------|----------|----------|
| GET | `/api/movies/` | Список всех фильмов |
| GET | `/api/movies/{id}/` | Детали фильма и его сеансы |
| GET | `/api/sessions/` | Список всех сеансов |
| GET | `/api/sessions/{id}/seats/` | Схема зала для конкретного сеанса |
| POST | `/api/bookings/` | Создать новое бронирование |
| GET | `/api/bookings/` | Список броней текущего пользователя |
| POST | `/api/users/register/` | Зарегистрировать нового пользователя |
| POST | `/api/users/login/` | Войти в систему (получить JWT-токен) |

---

# 👤 Роли и права доступа

## Администратор (`admin`)

- Имеет полный доступ через Django Admin (`/admin`).
- Может управлять (создавать, редактировать, удалять) фильмами, залами, сеансами и ценами через API или админ-панель.

## Пользователь (`user`)

- Может просматривать фильмы и расписание.
- Может бронировать билеты и просматривать свои бронирования.

---

# 📎 Ссылки

**Фронтенд проекта:**  
[Movie Booking Frontend](https://github.com/Gala-knd/movie-booking-frontend)

cat > README.md << 'EOF'
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
---

## 🚀 Инструкция по развёртыванию и запуску (локально)

### Шаг 1: Клонирование репозитория
```bash
git clone https://github.com/Gala-knd/movie-booking-frontend.git
cd movie-booking-frontend
---
Шаг 2: Создание и активация виртуального окружения

**Для Windows (Git Bash):**
```bash
python -m venv venv
source venv/Scripts/activate--

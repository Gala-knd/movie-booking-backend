from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/movies/', include('movies.urls')),
    path('api/sessions/', include('shows.urls')),
    path('api/bookings/', include('bookings.urls')),
    path('api/users/', include('users.urls')),
]

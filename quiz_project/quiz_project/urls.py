# quiz_project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('manage/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('quiz.urls')),
    path('users/', include('users.urls')),
]
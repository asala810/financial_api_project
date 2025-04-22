
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('financial_app.urls')), #http://127.0.0.1:8000/api/"url from financial_app"
]


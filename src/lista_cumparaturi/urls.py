from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('produse/', include('apps.produse.urls')),
    path('', include('apps.core.urls')),
]

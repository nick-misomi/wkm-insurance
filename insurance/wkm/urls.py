from django.contrib import admin
from django.urls import path, include

from landing.views import home
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('plans/', include('plans.urls')),
    path('landing/', include('landing.urls')),
    path('blog/', include('blog.urls')),
]

from django.contrib import admin
from django.urls import path, include

import myapi.urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(myapi.urls))
]

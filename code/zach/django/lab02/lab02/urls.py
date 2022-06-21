from django.contrib import admin
from django.urls import path, include

import url_short.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('url_short.urls'))
]

from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^chatbot/', include('chatbot.urls', namespace='chatbot')),
]

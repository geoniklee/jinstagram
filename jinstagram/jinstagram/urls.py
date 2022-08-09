from django.urls import path
from content.views import Main

urlpatterns = [
    path('', Main.as_view())
]
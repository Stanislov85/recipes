from django.urls import path
from .views import recept_viems, home_viems


urlpatterns = [
    path('',home_viems, name = 'home'),
    path('<recept>/',recept_viems, name = 'recept')
]
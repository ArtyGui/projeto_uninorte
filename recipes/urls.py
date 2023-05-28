from django.urls import path
from recipes.views import home,episodio,cadastro



urlpatterns = [
    path('',home),
    path('episodio/',episodio),
    path('cadastro/',cadastro)    
]

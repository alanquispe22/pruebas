from django.urls import path
from . import views

app_name = 'perfil'
urlpatterns = [
    # ex: perfil/
    path('perfil/',views.perfil, name="perfil"),
]
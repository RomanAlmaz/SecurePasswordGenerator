from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pass/', views.password_generator, name='password_generator'),
    path('word/', views.word_generator, name='word_generator'),
    path('set-language/', views.set_language, name='set_language'),
]

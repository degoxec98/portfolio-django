from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views


urlpatterns = [
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('signup/', views.signup, name="signup"),
    path(r'index/<str:username>', views.index, name="index"),
    path(r'proyecto/<int:id>', views.proyecto, name="proyecto"),
    path(r'portfolio/<int:id>', views.portfolio, name="portfolio"),
]
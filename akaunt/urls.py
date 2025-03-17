from django.urls import path
from .import views
from .views import  profile

app_name = 'akaunt'
urlpatterns = [
    path('register/' , views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', profile, name='profile'),
]
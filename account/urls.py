from django.urls import path
from . import views

urlpatterns = [
   path('', views.register, name='register'),
   path('login/', views.user_login, name='user-login'),
   path('logout/', views.user_logout, name='user-logout'),
   path('edit_profile/', views.edit_profile, name='edit_profile'),

]

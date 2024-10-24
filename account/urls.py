from django.urls import path
from . import views
from core.views import wallet_info

app_name = 'account'

urlpatterns = [
  path('register/', views.wallet_info, name='register'),
  path('login/', views.wallet_info, name='login'),
  path('profile/', views.wallet_info, name='profile'),
  path('logout/', views.wallet_info, name='logout'),
  path('deposit/', views.wallet_info, name='deposit'),
  path('spend/', views.wallet_info, name='spend'),
  path('transactions/', views.wallet_info, name='transactions'),
  path('change-password/', views.wallet_info, name='change_password'),

]
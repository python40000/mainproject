from Home import views
from django.urls import path
app_name='Home'

urlpatterns = [
    path('', views.home, name=''),
    path('show/', views.show, name='show'),
    path('reg/', views.reg, name='reg'),
    path('delete/<int:fid>', views.delete, name='delete'),
    path('edit/<int:fid>', views.edit, name='edit'),
    path('login/', views.login, name='login'),
]
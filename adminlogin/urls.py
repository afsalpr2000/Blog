from django.urls import path
from .views import Admin_Login

urlpatterns = [
    path('', Admin_Login, name='admin_login'),

]

from django.urls import path
from user_management.views import *

app_name = 'user_management'

urlpatterns = [
    path('register', RegisterView.as_view(), name='register'),
    path('login', LoginView.as_view(), name='login'),
    path('user-information/<uuid:user_id>/', GetUser.as_view(), name='get-user-information'),
]

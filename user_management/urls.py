
from django.urls import path
from user_management.views import *

app_name = 'user_management'

urlpatterns = [
    path('register', RegisterView.as_view(), name='register'),
    path('login', LoginView.as_view(), name='login'),
    path('user-information/<slug:query_type>', GetUser.as_view()),
    path('change-password/', ChangePasswordView.as_view()),
    path('update-profile/', UpdateUserView.as_view()),
]

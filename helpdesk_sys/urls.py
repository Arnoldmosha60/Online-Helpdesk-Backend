from django.urls import path
from .views import *

app_name = 'helpdesk_sys'

urlpatterns = [
    path('issues/', IssueListCreateView.as_view(), name='issue-list-create'),
    path('issues/<uuid:user_id>/', IssueDetailView.as_view(), name='issue-detail'),
]
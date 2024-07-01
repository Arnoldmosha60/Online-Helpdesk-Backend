from django.urls import path
from .views import *

app_name = 'helpdesk_sys'

urlpatterns = [
    path('issues/', IssueListCreateView.as_view(), name='issue-list-create'),
    path('issues/<uuid:user_id>/', IssueDetailView.as_view(), name='issue-detail'),
    path('issue-response/', IssueResponseCreateUpdateView.as_view(), name='issue-response-create'),
    path('issue-response/<uuid:pk>/', IssueResponseCreateUpdateView.as_view(), name='issue-response-update'),
    path('get-issue-responses/', IssueResponseListView.as_view(), name='get_all_issue_response'),
]
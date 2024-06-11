from django.db import models
import uuid
from user_management.models import User

# Create your models here.
class Issue(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    issue_description = models.CharField(max_length=500)
    category = models.CharField(max_length=50)
    urgency_level = models.CharField(max_length=20)
    submitted_on = models.DateTimeField(auto_now=True)
    issued_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id} - {self.issued_by.fullname}"

    class Meta:
        db_table = 'issue'

class IssueResponse(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.CharField(max_length=500)
    reply_date = models.DateTimeField(auto_now=True)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id} - {self.issue.id}"

    class Meta:
        db_table = 'issueresponse'

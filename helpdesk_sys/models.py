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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status=models.BooleanField(default=False)

    def __str__(self):
        return f"{self.id} => {self.user.id}"

    class Meta:
        db_table = 'issue'

class IssueResponse(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    response = models.CharField(max_length=500)
    reply_date = models.DateTimeField(auto_now=True)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id} - {self.issue.id}"

    class Meta:
        db_table = 'issueresponse'


class Feedback(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    response = models.ForeignKey('IssueResponse', on_delete=models.CASCADE)
    feedback_text = models.TextField()
    submitted_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id} - {self.response.id}"

    class Meta:
        db_table = 'feedback'

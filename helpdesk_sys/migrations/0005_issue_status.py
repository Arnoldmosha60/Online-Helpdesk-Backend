# Generated by Django 5.0.6 on 2024-06-14 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helpdesk_sys', '0004_rename_issued_by_issue_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
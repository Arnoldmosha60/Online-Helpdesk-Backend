# Generated by Django 5.0.6 on 2024-06-14 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='userType',
            field=models.PositiveIntegerField(choices=[(1, 'System Admin'), (2, 'System User')], default=2),
        ),
    ]

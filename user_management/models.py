from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
import uuid

class CustomUserManager(BaseUserManager):
    def create_user(self, email, fullname, contact, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, fullname=fullname, contact=contact, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, fullname, contact, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('userType', User.ADMIN)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, fullname, contact, password, **extra_fields)

class User(AbstractUser):
    ADMIN = 1
    USER = 2

    ROLE_CHOICES = (
        (ADMIN, "System Admin"),
        (USER, "System User"),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fullname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    contact = models.CharField(max_length=12)
    created_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    userType = models.PositiveIntegerField(choices=ROLE_CHOICES, default=USER)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["fullname", "contact"]

    objects = CustomUserManager()  # Set the custom user manager

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'user'
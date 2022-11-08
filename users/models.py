from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from choices.choices import USER_ROLES


class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password, **other_fields):
        if not email:
            raise ValueError("You must provide an email")
        email = self.normalize_email(email)

        user = self.model(
            email=email, username=username, **other_fields
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, username, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
        if other_fields.get('is_superuser') is not True:
            return ValueError(
                'Superuser must be assigned to is_staff=True'
            )

        if other_fields.get('is_superuser') is not True:
            return ValueError(
                'Superuser must be assigned to is_superuser=True'
            )

        return self.create_user(email, username, password, **other_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    list_filter = 'user_role'
    id = models.AutoField(primary_key=True,db_column='user_id')
    email = models.EmailField(unique=True, db_column="user_email")
    username = models.CharField(
        max_length=200, unique=True, db_column="user_name")
    password = models.CharField(max_length=200, db_column="user_password")
    user_national_id = models.IntegerField(default=0)
    user_phone = models.CharField(max_length=100, default="")
    user_role = models.CharField(
        max_length=10, choices=USER_ROLES, blank=True)
    is_superuser = models.BooleanField(
        default=False, db_column="user_is_superuser")
    is_staff = models.BooleanField(
        default=False, db_column="user_is_staff")
    is_active = models.BooleanField(
        default=True, db_column="user_is_active")
    last_login = models.DateTimeField(
        blank=True, null=True, db_column="user_last_login")
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','user_phone','user_national_id']

    def __str__(self):
        return self.username


class Farmer(models.Model):
    farmer_id = models.AutoField(primary_key=True)
    farmer_user_id = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.farmer_user_id.username


class Merchant(models.Model):
    merchant_id = models.AutoField(primary_key=True)
    merchant_user_id = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.merchant_user_id.username

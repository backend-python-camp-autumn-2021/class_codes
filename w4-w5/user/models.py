from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager, BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, email, password, phone, **extra_fields):

        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, phone=phone, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, phone,  **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password,phone, **extra_fields)


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=250)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone']
    objects = CustomUserManager()

    class Meta:
        db_table = 'auth_user'
        verbose_name = _('user')
        verbose_name_plural = _('users')

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.RESTRICT)
    phone = models.CharField(max_length=11, unique=True)
    image = models.ImageField(upload_to='profile/', null=True, blank=True)


    def __str__(self):
        return self.user.email

    def number_address(self):
        return len(self.address.all())

    def save(self, *args, **kwargs):
        if not self.phone:
            raise ValueError("telephon lazeme!")
        if not self.user:
            user_obj = User.objects.create(username=self.phone)
            self.user = user_obj
        return super(Profile, self).save(*args, **kwargs)


class UserAddress(models.Model):
    user = models.ForeignKey(
        Profile, related_name='address', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.user.username} - priority: {self.priority_address}"
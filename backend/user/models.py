from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

from company.models import Company
from user.choices import USER_ROLES, CLIENT, SUPER_ADMIN, ADMIN


class MyUser(AbstractUser):
    first_name = models.CharField('first name', max_length=50, blank=False, null=False, default='username')
    last_name = models.CharField('last name', max_length=50, blank=False, null=False, default='username')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    telephone_number = models.CharField(max_length=13, blank=False, null=False, default='phone_number')
    user_type = models.CharField(max_length=11,
                                 choices=USER_ROLES,
                                 default=CLIENT)
    company = models.ForeignKey(Company, blank=True, null=True, on_delete=models.CASCADE)
    avatar = models.ImageField(default="", null=True, blank=True, upload_to='src/images')
    is_staff = models.BooleanField(default=False)

    class Meta:
        db_table = 'user'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__original_name = self.username

    def save(self, *args, **kwargs):
        if self.username != self.__original_name:
            self.date_updated = timezone.now()

        if not self.is_staff:
            self.user_type = CLIENT
        else:
            self.user_type = ADMIN
        if self.is_superuser:
            self.user_type = SUPER_ADMIN
        super().save(*args, **kwargs)
        self.__original_name = self.username

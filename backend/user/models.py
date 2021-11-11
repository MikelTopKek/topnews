from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

from company.models import Company


class MyUser(AbstractUser):
    first_name = models.CharField('first name', max_length=50, blank=False, null=False, default='username')
    last_name = models.CharField('last name', max_length=50, blank=False, null=False, default='username')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    telephone_number = models.CharField(max_length=13, blank=False, null=False, default='phone_number')
    user_type = models.CharField(max_length=2,
                                 choices=(
                                     ('CL', 'CLIENT'),
                                     ('AD', 'ADMIN'),
                                     ('SP', 'SUPER_ADMIN')
                                 ))
    company_id = models.ForeignKey(Company, blank=True, null=True, on_delete=models.CASCADE)
    avatar = models.ImageField(default="", null=True, blank=True, upload_to='src/images')

    class Meta:
        db_table = 'user'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__original_name = self.username

    def save(self, *args, **kwargs):
        if self.username != self.__original_name:
            self.date_updated = timezone.now()
        super().save(*args, **kwargs)
        self.__original_name = self.username

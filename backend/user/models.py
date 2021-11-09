from django.contrib.auth.models import AbstractUser
from django.db import models


class MyUser(AbstractUser):
    first_name = models.CharField('first name', max_length=50, blank=False, null=False, default='username', unique=True)
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
    # TODO::: add Company
    # company_id = models.ForeignKey('Company', blank=True, null=True, on_delete=models.CASCADE)
    # TODO::: add avatar

    class Meta:
        db_table = 'user'

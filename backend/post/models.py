from django.db import models

from company.models import Company
from user.models import MyUser


class Post(models.Model):
    title = models.CharField(max_length=50, blank=False, null=False, unique=True)
    user_id = models.ForeignKey(MyUser, blank=True, null=True, on_delete=models.CASCADE)
    company_id = models.ForeignKey(Company, blank=True, null=True, on_delete=models.CASCADE)
    text = models.CharField(max_length=30, blank=False, null=False, unique=True)
    topic = models.CharField(max_length=50, blank=False, null=False, unique=True)

    class Meta:
        db_table = 'post'

    def __str__(self):
        return f"Post {self.title}"

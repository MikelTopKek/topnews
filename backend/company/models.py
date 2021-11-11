from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=20, blank=False, null=False, unique=True)
    url = models.CharField(max_length=120, blank=False, null=False, unique=True)
    address = models.CharField(max_length=50, blank=False, null=False, unique=True)
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    logo = models.ImageField(default="", null=True, blank=True, upload_to='src/images')

    class Meta:
        db_table = 'company'

    def __str__(self):
        return str({self.name})

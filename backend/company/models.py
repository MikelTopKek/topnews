from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False, unique=True)
    url = models.CharField(max_length=120, blank=False, null=False, unique=True)
    address = models.CharField(max_length=30, blank=False, null=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    # TODO::: add logo

    class Meta:
        db_table = 'company'

    def __str__(self):
        return f"Company {self.name}"

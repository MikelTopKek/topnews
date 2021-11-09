from django.contrib import admin

from user.models import MyUser


@admin.register(MyUser)
class UserAdmin(admin.ModelAdmin):
    fields = ('first_name', 'last_name', 'telephone_number', 'user_type')
    exclude = ('password',)

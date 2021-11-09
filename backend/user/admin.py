from django.contrib import admin

from company.models import Company
from post.models import Post
from user.models import MyUser


@admin.register(MyUser)
class UserAdmin(admin.ModelAdmin):
    fields = ('first_name', 'last_name', 'telephone_number', 'user_type')
    exclude = ('password',)


admin.site.register(Company)
admin.site.register(Post)

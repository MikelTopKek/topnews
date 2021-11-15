import random

from django.contrib.auth import get_user_model
from django.db import migrations

from company.models import Company
from post.models import Post

UserModel = get_user_model()


def delete_everything():
    UserModel.objects.all().delete()
    Post.objects.all().delete()
    Company.objects.all().delete()


def init_db_data(apps, schema_editor):
    """Delete all previous records in db """
    delete_everything()

    data = {'number_of_users': 200, 'posts_per_user': 30, 'number_of_companies': 10}
    post_id = 0
    user_id = 0
    company_id = 0

    for company in range(data['number_of_companies']):
        company_id += 1
        company_data = {
            'name': f'name-title{company_id}',
            'url': f'url-text{company_id}',
            'address': f'address-topic{company_id}'
        }
        Company.objects.create(**company_data)

    for users in range(int(data['number_of_users'])):
        user_id += 1
        user_data = {
            'username': f'UserName{user_id}',
            'first_name': f'first_name{user_id}',
            'last_name': f'first_name{user_id}',
            'email': f'some-email{user_id}@gmail.com',
            'telephone_number': '+380954527680',
            'password': 'password',
            'is_staff': False,
            'is_superuser': False,
            'company': Company.objects.get(id=random.randint(1, data['number_of_companies']))
        }
        UserModel.objects.create(**user_data)
        for posts in range(random.randint(1, int(data['posts_per_user']))):
            post_id += 1
            post_data = {
                'title': f'Post-title {post_id}',
                'text': f'Text {post_id}',
                'topic': f'Topic {post_id}',
                'user': UserModel.objects.get(id=user_id)
            }
            Post.objects.create(**post_data)


class Migration(migrations.Migration):

    dependencies = []

    operations = [
        migrations.RunSQL('ALTER SEQUENCE user_id_seq RESTART WITH 1'),
        migrations.RunSQL('ALTER SEQUENCE post_id_seq RESTART WITH 1'),
        migrations.RunSQL('ALTER SEQUENCE company_id_seq RESTART WITH 1'),
        migrations.RunPython(init_db_data)
    ]

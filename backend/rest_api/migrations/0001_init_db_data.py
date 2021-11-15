import os
import random

from django.contrib.auth import get_user_model
from django.db import migrations

from company.models import Company
from post.models import Post
from utils.env_utils import load_env

UserModel = get_user_model()


def create_super_user():
    user_data = {
        'username': 'admin',
        'first_name': 'admin',
        'last_name': 'admin',
        'email': 'admin@gmail.com',
        'telephone_number': '+380950000000',
        'password': 'password',
    }
    user = UserModel.objects.create_superuser(**user_data, is_active=True)
    user.save()


def delete_everything():
    UserModel.objects.all().delete()
    Post.objects.all().delete()
    Company.objects.all().delete()


def init_db_data(apps, schema_editor):
    """Delete all previous records in db """
    delete_everything()
    create_super_user()

    data = {'number_of_users': 200, 'posts_per_user': 30, 'number_of_companies': 10}

    for company_id in range(data['number_of_companies']):
        company_data = {
            'name': f'name-title{company_id}',
            'url': f'url-text{company_id}',
            'address': f'address-topic{company_id}'
        }
        company = Company.objects.create(**company_data)
        company.save()

    for user_id in range(1, data['number_of_users']):
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
        user = UserModel.objects.create(**user_data)
        user.save()

        for post_id in range(data['posts_per_user']):
            post_data = {
                'title': f'Post-title {user_id}-{post_id}',
                'text': f'Text {user_id}-{post_id}',
                'topic': f'Topic {user_id}-{post_id}',
                'user': UserModel.objects.get(id=user_id)
            }
            post = Post.objects.create(**post_data)
            post.save()


load_env()


class Migration(migrations.Migration):

    dependencies = []

    operations = [
        migrations.RunSQL('ALTER SEQUENCE user_id_seq RESTART WITH 1'),
        migrations.RunSQL('ALTER SEQUENCE post_id_seq RESTART WITH 1'),
        migrations.RunSQL('ALTER SEQUENCE company_id_seq RESTART WITH 1'),
        migrations.RunPython(init_db_data)
    ] if os.getenv('environment_type') == 'local' else []


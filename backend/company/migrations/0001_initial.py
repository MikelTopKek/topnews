# Generated by Django 3.2.6 on 2021-11-15 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('url', models.CharField(max_length=120, unique=True)),
                ('address', models.CharField(max_length=50, unique=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('logo', models.ImageField(blank=True, default='', null=True, upload_to='src/images')),
            ],
            options={
                'db_table': 'company',
            },
        ),
    ]

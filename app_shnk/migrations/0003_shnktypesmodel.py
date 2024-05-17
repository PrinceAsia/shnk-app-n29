# Generated by Django 5.0.4 on 2024-05-09 14:21

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_shnk', '0002_shnkgroupsmodel'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SHNKTypesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('type_name_uz', models.CharField(max_length=10, unique=True)),
                ('type_name_ru', models.CharField(max_length=10, null=True, unique=True)),
                ('type_description_uz', models.CharField(max_length=255, null=True)),
                ('type_description_ru', models.CharField(max_length=255, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'SHNK types',
                'db_table': 'shnk_types',
            },
        ),
    ]

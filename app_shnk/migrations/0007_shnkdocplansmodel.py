# Generated by Django 5.0.4 on 2024-05-11 13:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_shnk', '0006_shnkdocpartsmodel'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SHNKDocPlansModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('plan_title_uz', models.CharField(max_length=255, unique=True)),
                ('plan_title_ru', models.CharField(max_length=255, null=True, unique=True)),
                ('plan_number', models.IntegerField()),
                ('plan_text_uz', models.CharField(max_length=255, null=True)),
                ('plan_text_ru', models.CharField(max_length=255, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('plan_document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_shnk.shnkdocumentsmodel')),
                ('plan_part', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_shnk.shnkdocpartsmodel')),
            ],
            options={
                'verbose_name_plural': 'SHNK Document PLans',
                'db_table': 'shnk_doc_plans',
            },
        ),
    ]

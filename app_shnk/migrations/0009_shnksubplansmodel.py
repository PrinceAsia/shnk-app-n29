# Generated by Django 5.0.4 on 2024-05-11 14:33

import ckeditor.fields
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_shnk', '0008_shnkdocpartsmodel_has_plan_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SHNKSubPlansModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('sub_plan_title_uz', models.CharField(max_length=255, unique=True)),
                ('sub_plan_title_ru', models.CharField(max_length=255, null=True, unique=True)),
                ('sub_plan_number', models.IntegerField()),
                ('sub_plan_text_uz', ckeditor.fields.RichTextField()),
                ('sub_plan_text_ru', ckeditor.fields.RichTextField(null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('sub_plan_document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_shnk.shnkdocumentsmodel')),
                ('sub_plan_plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_shnk.shnkdocplansmodel')),
            ],
            options={
                'verbose_name_plural': 'SHNK Sub PLans',
                'db_table': 'shnk_sub_plans',
            },
        ),
    ]
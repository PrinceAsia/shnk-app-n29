# Generated by Django 5.0.4 on 2024-05-16 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_shnk', '0009_shnksubplansmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='shnkdocumentsmodel',
            name='shnk_rating',
            field=models.JSONField(default=list),
        ),
    ]

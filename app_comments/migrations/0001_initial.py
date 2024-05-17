# Generated by Django 5.0.4 on 2024-05-14 13:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_shnk', '0009_shnksubplansmodel'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.TextField()),
                ('comment_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('comment_dislikes', models.ManyToManyField(blank=True, related_name='comment_dislikes', to=settings.AUTH_USER_MODEL)),
                ('comment_doc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_shnk.shnkdocumentsmodel')),
                ('comment_likes', models.ManyToManyField(blank=True, related_name='comment_likes', to=settings.AUTH_USER_MODEL)),
                ('comment_reply', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_comments.comment')),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
                'db_table': 'comments',
                'ordering': ['comment_date'],
            },
        ),
    ]

# Generated by Django 4.1.3 on 2022-11-21 17:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0004_user_experiencia'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='usuario',
        ),
        migrations.AddField(
            model_name='user',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]

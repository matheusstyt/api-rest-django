# Generated by Django 4.1.3 on 2022-11-21 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiencia', '0001_initial'),
        ('user', '0003_remove_user_formacao_academica_user_formacao'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='experiencia',
            field=models.ManyToManyField(to='experiencia.experiencia'),
        ),
    ]

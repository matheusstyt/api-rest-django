# Generated by Django 4.1.3 on 2022-11-21 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Formacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instituicao_ensino', models.CharField(max_length=70)),
                ('diploma', models.CharField(max_length=70)),
                ('area_estudo', models.CharField(max_length=70)),
                ('mes_inicio', models.CharField(max_length=70)),
                ('ano_inicio', models.CharField(max_length=70)),
                ('mes_fim', models.CharField(max_length=70)),
                ('ano_fim', models.CharField(max_length=70)),
                ('nota', models.CharField(max_length=70)),
                ('atividades', models.TextField(max_length=500)),
                ('descricao', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Sobre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.TextField(max_length=2600)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=50)),
                ('nome', models.CharField(max_length=50)),
                ('sobrenome', models.CharField(max_length=50)),
                ('nomesocial', models.CharField(max_length=50, null=True)),
                ('bio', models.TextField()),
                ('titulo', models.CharField(max_length=150)),
                ('local', models.CharField(max_length=50)),
                ('pais', models.CharField(max_length=50)),
                ('cidade', models.CharField(max_length=50)),
                ('formacao_academica', models.CharField(max_length=50)),
                ('setor', models.CharField(max_length=50)),
                ('cargo', models.CharField(max_length=50, null=True)),
                ('exibir_a_empresa_atual_na_minha_introdução', models.BooleanField()),
                ('exibir_formação_na_minha_introdução', models.BooleanField()),
            ],
        ),
    ]
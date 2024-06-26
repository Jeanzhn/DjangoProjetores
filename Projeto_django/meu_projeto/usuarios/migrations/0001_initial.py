# Generated by Django 5.0.6 on 2024-06-11 18:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False, verbose_name='user.id')),
                ('nome', models.CharField(default='nome padrao', max_length=100, verbose_name='nome-professor')),
                ('materia', models.CharField(default='Materia Padrao', max_length=100, verbose_name='materia-professor')),
                ('sala', models.CharField(max_length=3, verbose_name='sala')),
            ],
            options={
                'verbose_name': 'Professor',
                'verbose_name_plural': 'Professores',
            },
        ),
        migrations.CreateModel(
            name='datashow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=100)),
                ('quantidade', models.PositiveIntegerField()),
                ('reservado', models.BooleanField(default=False)),
                ('Professor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='usuarios.professor')),
            ],
        ),
    ]

# Generated by Django 5.1.2 on 2024-11-15 11:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='forum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='anonymous', max_length=200)),
                ('email', models.CharField(max_length=200, null=True)),
                ('topic', models.CharField(max_length=300)),
                ('description', models.CharField(blank=True, max_length=1000)),
                ('link', models.CharField(max_length=100, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Discussion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discuss', models.CharField(max_length=1000)),
                ('forum', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='forum.forum')),
            ],
        ),
    ]
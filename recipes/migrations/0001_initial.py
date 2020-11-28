# Generated by Django 3.0.5 on 2020-11-28 00:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=300)),
                ('description', models.TextField(default=None)),
                ('course_type', models.CharField(default=None, max_length=150)),
                ('difficulty', models.CharField(max_length=100)),
                ('cooking_method', models.CharField(default=None, max_length=150)),
                ('cost', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredients', to='recipes.Recipe')),
            ],
        ),
    ]

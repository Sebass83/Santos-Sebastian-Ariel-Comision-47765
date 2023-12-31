# Generated by Django 4.2.5 on 2023-10-01 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('description', models.CharField(max_length=400)),
                ('entryDate', models.DateField(auto_now_add=True)),
                ('min_img_url', models.URLField(blank=True)),
                ('author', models.CharField(max_length=40)),
            ],
        ),
    ]

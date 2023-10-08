# Generated by Django 4.2.5 on 2023-10-07 23:56

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CodigoCreativoApp', '0013_alter_blog_body_alter_blog_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mensajes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('de', models.CharField(max_length=150)),
                ('para', models.CharField(max_length=150)),
                ('asunto', models.CharField(max_length=150)),
                ('body', ckeditor.fields.RichTextField(default=None)),
                ('leido', models.BooleanField(default=False)),
            ],
        ),
    ]

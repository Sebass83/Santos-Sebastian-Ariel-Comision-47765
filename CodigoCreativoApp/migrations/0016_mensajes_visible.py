# Generated by Django 4.2.5 on 2023-10-10 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CodigoCreativoApp', '0015_alter_blog_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='mensajes',
            name='visible',
            field=models.BooleanField(default=True),
        ),
    ]

# Generated by Django 4.2.5 on 2023-10-07 00:29

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CodigoCreativoApp', '0010_blog_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='body',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]

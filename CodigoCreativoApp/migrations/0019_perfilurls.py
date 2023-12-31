# Generated by Django 4.2.5 on 2023-10-11 20:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('CodigoCreativoApp', '0018_remove_mensajes_leido_remove_mensajes_spam_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PerfilURLS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_github', models.URLField(blank=True)),
                ('url_linkedin', models.URLField(blank=True)),
                ('url_personal', models.URLField(blank=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

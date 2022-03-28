# Generated by Django 4.0.3 on 2022-03-08 19:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, max_length=10, null=True, verbose_name='Telefon Numarası')),
                ('date_birth', models.DateField(blank=True, null=True, verbose_name='Doğum Tarihi')),
                ('gender', models.PositiveSmallIntegerField(blank=True, choices=[(0, 'Erkek'), (1, 'Kadın'), (2, 'Diğerleri')], null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Kullanıcı')),
            ],
        ),
    ]

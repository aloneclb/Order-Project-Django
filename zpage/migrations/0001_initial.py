# Generated by Django 4.0.3 on 2022-03-07 07:51

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('slug', models.SlugField(editable=False, unique=True)),
                ('status', models.PositiveIntegerField(choices=[(0, 'Taslak'), (1, 'Yayınla'), (2, 'Sil')])),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Hakkımızda Ayarları',
                'ordering': ('-update_time',),
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=50)),
                ('message', models.TextField(blank=True, max_length=255)),
                ('phone', models.CharField(max_length=50)),
                ('ip', models.CharField(default='Ip Belirtilmedi', max_length=50)),
                ('status', models.CharField(choices=[('New', 'Yeni'), ('Read', 'Okundu'), ('Important', 'Önemli'), ('Close', 'Cevap Verildi')], default='New', max_length=10)),
                ('note', models.CharField(default='Not Alınmadı', max_length=70)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='SiteSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('site_welcome', models.CharField(blank=True, max_length=50, null=True)),
                ('keywords', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('company', models.CharField(blank=True, max_length=50, null=True)),
                ('address', models.TextField(blank=True, max_length=150, null=True)),
                ('phone', models.CharField(blank=True, max_length=150, null=True)),
                ('fax', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.CharField(blank=True, max_length=60, null=True)),
                ('smtpserver', models.CharField(blank=True, max_length=50, null=True)),
                ('smtpemail', models.CharField(blank=True, max_length=50, null=True)),
                ('smtppassword', models.CharField(blank=True, max_length=50, null=True)),
                ('smtpport', models.CharField(blank=True, max_length=9, null=True)),
                ('icon', models.ImageField(blank=True, upload_to='SiteIcon/%Y/%m/%d/')),
                ('facebook', models.CharField(blank=True, max_length=255, null=True)),
                ('instagram', models.CharField(blank=True, max_length=255, null=True)),
                ('twitter', models.CharField(blank=True, max_length=255, null=True)),
                ('references', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.PositiveIntegerField(choices=[(0, 'Taslak'), (1, 'Yayınla'), (2, 'Sil')])),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner', models.ImageField(default='banner/default.png', help_text='Fotoğrafın 1296x512 Piksel Boyutunda Olması Gerekiyor', upload_to='banner/', verbose_name='Banner Fotoğrafı')),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('link', models.CharField(blank=True, max_length=200, null=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Slider Ayarları',
                'ordering': ('-created_time',),
            },
        ),
    ]
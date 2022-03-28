# Generated by Django 4.0.3 on 2022-03-08 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zcard', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orderitem',
            options={'ordering': ('-update_date',), 'verbose_name_plural': 'Sepete eklenen Ürünler'},
        ),
        migrations.AddField(
            model_name='order',
            name='ref_code',
            field=models.CharField(blank=True, max_length=12, null=True, unique=True),
        ),
    ]

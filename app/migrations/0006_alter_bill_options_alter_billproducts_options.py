# Generated by Django 5.0.1 on 2024-01-15 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_bill_billproducts'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bill',
            options={'verbose_name': 'Çekler'},
        ),
        migrations.AlterModelOptions(
            name='billproducts',
            options={'verbose_name': 'Çek element', 'verbose_name_plural': 'Çek elementleri'},
        ),
    ]

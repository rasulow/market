# Generated by Django 5.0.1 on 2024-01-12 18:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_remove_product_img_alter_product_short_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'bill',
            },
        ),
        migrations.CreateModel(
            name='BillProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.FloatField()),
                ('total_price', models.FloatField()),
                ('bill', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.bill')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.product')),
            ],
            options={
                'db_table': 'bill_products',
            },
        ),
    ]

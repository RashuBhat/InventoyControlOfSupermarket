# Generated by Django 3.1.3 on 2020-12-08 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supermarket_app', '0006_manager'),
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('item_id', models.IntegerField(primary_key=True, serialize=False)),
                ('price', models.DecimalField(decimal_places=2, max_digits=4)),
                ('item_name', models.CharField(max_length=50)),
                ('brand', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'Items',
            },
        ),
    ]

# Generated by Django 3.1.1 on 2020-09-25 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testmerchantapp', '0007_merchanttestpage_gateway_mode'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MerchantTestPage',
        ),
    ]
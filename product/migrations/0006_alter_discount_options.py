# Generated by Django 3.2.5 on 2021-08-07 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20210807_1654'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='discount',
            options={'ordering': ('title',), 'verbose_name_plural': 'Discounts'},
        ),
    ]

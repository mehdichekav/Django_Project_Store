# Generated by Django 3.2.5 on 2021-08-08 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0006_alter_address_lng'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={},
        ),
        migrations.AlterField(
            model_name='address',
            name='description',
            field=models.TextField(blank=True, help_text='enter your description', null=True, verbose_name='description'),
        ),
    ]

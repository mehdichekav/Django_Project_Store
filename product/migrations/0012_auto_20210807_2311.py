# Generated by Django 3.2.5 on 2021-08-07 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_auto_20210807_2035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discount',
            name='Cash',
            field=models.CharField(help_text='enter your Cash', max_length=100, verbose_name='Cash'),
        ),
        migrations.AlterField(
            model_name='discount',
            name='Deduction_from_the_price',
            field=models.CharField(help_text='enter your Deduction_from_the_price', max_length=100, verbose_name='Deduction_from_the_price'),
        ),
    ]

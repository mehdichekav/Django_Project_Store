# Generated by Django 3.2.5 on 2021-08-07 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_of_birth',
            field=models.DateField(blank=True, help_text='enter your date_of_birth', null=True, verbose_name='date_of_birth'),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, help_text='enter your first_name', max_length=100, null=True, verbose_name='first_name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, help_text='enter your last_name', max_length=100, null=True, verbose_name='last_name'),
        ),
    ]
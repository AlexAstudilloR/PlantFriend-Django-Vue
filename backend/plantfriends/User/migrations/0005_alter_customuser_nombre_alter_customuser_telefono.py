# Generated by Django 5.1.1 on 2024-10-22 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0004_customuser_is_active_customuser_is_staff_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='nombre',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='telefono',
            field=models.CharField(blank=True, default='', max_length=15),
        ),
    ]
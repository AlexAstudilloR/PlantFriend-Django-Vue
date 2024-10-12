# Generated by Django 5.1.1 on 2024-10-12 02:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Guides', '0002_alter_guides_descripcion'),
        ('Plants', '0004_alter_category_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Garden',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('guia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guides.guides')),
                ('planta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Plants.plants')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

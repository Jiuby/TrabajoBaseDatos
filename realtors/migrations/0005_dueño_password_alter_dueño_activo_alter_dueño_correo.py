# Generated by Django 5.2.1 on 2025-05-15 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0004_dueño_delete_realtor'),
    ]

    operations = [
        migrations.AddField(
            model_name='dueño',
            name='password',
            field=models.CharField(default=123456, max_length=128),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dueño',
            name='activo',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='dueño',
            name='correo',
            field=models.EmailField(max_length=50, unique=True),
        ),
    ]

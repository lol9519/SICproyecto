# Generated by Django 2.2.4 on 2019-11-03 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('informesContables', '0004_categoriacuentas_tipo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoriacuentas',
            name='tipo',
        ),
        migrations.AlterField(
            model_name='categoriacuentas',
            name='nombre',
            field=models.CharField(default='Activo', max_length=10),
        ),
    ]
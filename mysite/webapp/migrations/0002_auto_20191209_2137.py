# Generated by Django 3.0 on 2019-12-10 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='tipo_cliente',
            field=models.CharField(choices=[('Gobierno', 'Gobierno'), ('Particular', 'Particular'), ('Empresarial', 'Empresarial')], max_length=40, null=True),
        ),
    ]

# Generated by Django 3.0 on 2019-12-10 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NIT', models.CharField(max_length=40, null=True)),
                ('nombre', models.CharField(max_length=100, null=True)),
                ('direccion', models.CharField(max_length=200, null=True)),
                ('telefono', models.CharField(max_length=40, null=True)),
                ('email', models.CharField(max_length=100, null=True)),
                ('tipo_cliente', models.CharField(max_length=40, null=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]

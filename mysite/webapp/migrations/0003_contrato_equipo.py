# Generated by Django 3.0 on 2019-12-10 02:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20191209_2137'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=120, null=True)),
                ('tipo_equipo', models.CharField(choices=[('Impresora', 'Impresora'), ('Escritorio', 'Escritorio'), ('Portatil', 'Portatil'), ('Escaner', 'Escaner')], max_length=40, null=True)),
                ('serial', models.CharField(max_length=40, null=True)),
                ('marca', models.CharField(max_length=40, null=True)),
                ('proveedor', models.CharField(max_length=40, null=True)),
                ('caracteristicas', models.CharField(max_length=400, null=True)),
                ('condicion_equipo', models.CharField(choices=[('Dañado', 'Dañado'), ('Utilizable', 'Utilizable'), ('Reparado', 'Reparado'), ('EsperaRepuesto', 'EsperaRepuesto')], max_length=40, null=True)),
                ('anotaciones', models.CharField(max_length=100, null=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, null=True)),
                ('costo_reposicion', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contrato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nroContrato', models.CharField(max_length=30, null=True)),
                ('fecha_inicio', models.DateTimeField(auto_now_add=True, null=True)),
                ('fecha_terminacion', models.DateTimeField(auto_now_add=True, null=True)),
                ('responsable', models.CharField(max_length=100, null=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, null=True)),
                ('valor', models.FloatField(null=True)),
                ('estado_contrato', models.CharField(choices=[('En ejecucion', 'En ejecucion'), ('Terminado', 'Terminado'), ('Pendiente', 'Pendiente'), ('Cancelado', 'Cancelado')], max_length=60, null=True)),
                ('tecnico', models.CharField(choices=[('Ricardo Aleman', 'Ricardo Aleman'), ('Hernan Vidaure', 'Hernan Vidaure'), ('Jeyson Porras', 'Jeyson Porras'), ('Natalia Ramirez', 'Natalia Ramirez')], max_length=60, null=True)),
                ('cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='webapp.Cliente')),
                ('equipo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='webapp.Equipo')),
            ],
        ),
    ]

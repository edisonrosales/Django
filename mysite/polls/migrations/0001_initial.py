# Generated by Django 3.0.1 on 2019-12-23 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idEmpleado', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=60)),
                ('password', models.CharField(max_length=20)),
                ('edad', models.IntegerField()),
                ('sueldo', models.FloatField()),
                ('fechaNacimiento', models.DateField()),
                ('idDepartamento', models.CharField(max_length=20)),
                ('responsable', models.BooleanField()),
            ],
        ),
    ]
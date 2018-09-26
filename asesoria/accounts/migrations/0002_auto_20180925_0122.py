# Generated by Django 2.0.2 on 2018-09-25 06:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('codigo', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('correo', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AlterField(
            model_name='cita',
            name='nombreAlumno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Alumno'),
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]

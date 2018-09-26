# Generated by Django 2.0.1 on 2018-09-26 04:38

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0009_auto_20180926_0425'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='cita',
            unique_together={('asesoria', 'alumno')},
        ),
        migrations.AlterUniqueTogether(
            name='favorito',
            unique_together={('asesoria', 'alumno')},
        ),
    ]

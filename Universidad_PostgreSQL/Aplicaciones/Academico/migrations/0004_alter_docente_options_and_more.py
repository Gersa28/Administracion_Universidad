# Generated by Django 4.2 on 2023-04-07 20:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Academico', '0003_alter_curso_nombre'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='docente',
            options={'verbose_name': 'Docente', 'verbose_name_plural': 'Docentes'},
        ),
        migrations.RemoveField(
            model_name='docente',
            name='apellido_materno',
        ),
    ]

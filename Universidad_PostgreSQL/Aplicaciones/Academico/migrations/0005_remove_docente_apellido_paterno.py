# Generated by Django 4.2 on 2023-04-07 20:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Academico', '0004_alter_docente_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='docente',
            name='apellido_paterno',
        ),
    ]
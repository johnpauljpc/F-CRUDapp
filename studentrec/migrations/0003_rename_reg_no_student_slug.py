# Generated by Django 4.0.6 on 2022-09-13 13:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studentrec', '0002_student_reg_no'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='reg_no',
            new_name='slug',
        ),
    ]

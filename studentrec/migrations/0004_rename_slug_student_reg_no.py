# Generated by Django 4.0.6 on 2022-09-13 15:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studentrec', '0003_rename_reg_no_student_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='slug',
            new_name='reg_no',
        ),
    ]
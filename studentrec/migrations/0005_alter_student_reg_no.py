# Generated by Django 4.0.6 on 2022-09-13 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentrec', '0004_rename_slug_student_reg_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='reg_no',
            field=models.SlugField(unique=True),
        ),
    ]

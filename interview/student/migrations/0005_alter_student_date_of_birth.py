# Generated by Django 3.2.18 on 2023-04-19 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_alter_student_roll_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='date_of_birth',
            field=models.DateField(),
        ),
    ]
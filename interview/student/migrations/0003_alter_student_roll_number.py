# Generated by Django 3.2.18 on 2023-04-19 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_alter_student_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='roll_number',
            field=models.IntegerField(),
        ),
    ]

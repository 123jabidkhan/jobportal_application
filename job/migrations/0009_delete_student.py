# Generated by Django 3.1.5 on 2021-02-07 17:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0008_student_username'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Student',
        ),
    ]
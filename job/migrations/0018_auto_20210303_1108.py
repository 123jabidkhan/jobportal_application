# Generated by Django 3.1.5 on 2021-03-03 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0017_remove_job_recruiter'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='creation_date',
        ),
        migrations.AlterField(
            model_name='job',
            name='end_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='start_date',
            field=models.DateField(null=True),
        ),
    ]

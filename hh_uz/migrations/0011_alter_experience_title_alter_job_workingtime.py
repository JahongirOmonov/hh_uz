# Generated by Django 4.2.7 on 2024-02-21 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hh_uz', '0010_job_workingtime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='title',
            field=models.CharField(choices=[('Inexperienced', 'Inexperienced'), ('Between 1 and 3 years', 'Between 1 and 3 years'), ('Between 3 and 6 years', 'Between 3 and 6 years'), ('More 6 years', 'More 6 years'), ('Unimportant', 'Unimportant')], default='Inexperienced', max_length=31),
        ),
        migrations.AlterField(
            model_name='job',
            name='workingTime',
            field=models.CharField(choices=[('FULL', 'Full time'), ('HALF', 'Half day')], default='FULL', max_length=10),
        ),
    ]
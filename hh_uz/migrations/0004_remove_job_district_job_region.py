# Generated by Django 4.2.7 on 2024-02-20 23:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hh_uz', '0003_remove_district_neighbour_region_neighbour'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='district',
        ),
        migrations.AddField(
            model_name='job',
            name='region',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='hh_uz.region'),
            preserve_default=False,
        ),
    ]

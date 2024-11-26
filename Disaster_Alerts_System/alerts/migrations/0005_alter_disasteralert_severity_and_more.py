# Generated by Django 5.1.3 on 2024-11-26 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alerts', '0004_disasteralert_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disasteralert',
            name='severity',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='disasteralert',
            name='type',
            field=models.CharField(choices=[('flood', 'Flood'), ('earthquake', 'Earthquake'), ('storm', 'Storm'), ('wildfire', 'Wildfire')], max_length=50),
        ),
    ]

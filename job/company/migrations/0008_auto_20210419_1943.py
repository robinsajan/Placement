# Generated by Django 3.1.7 on 2021-04-19 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0007_job_hide_key'),
    ]

    operations = [
        migrations.RenameField(
            model_name='companyprofile',
            old_name='specialty',
            new_name='speciality',
        ),
    ]

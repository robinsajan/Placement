# Generated by Django 3.1.7 on 2021-04-12 10:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('student', '0010_auto_20210410_1841'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_title', models.CharField(max_length=200)),
                ('project_description', models.TextField()),
                ('Semester', models.CharField(choices=[('1', 'I'), ('2', 'II'), ('3', 'III'), ('4', 'IV'), ('5', 'V'), ('6', 'VI'), ('7', 'VII'), ('8', 'VII')], max_length=1)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
# Generated by Django 4.2.3 on 2023-09-01 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collegeapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teachermodel',
            name='t_phone',
            field=models.CharField(max_length=255),
        ),
    ]
# Generated by Django 4.0.2 on 2022-03-09 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_faculty_faculty_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='faculty',
            name='faculty_password',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='faculty_email',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]

# Generated by Django 3.0.2 on 2020-02-21 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('syllabus', '0004_auto_20200219_2303'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='pdf',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
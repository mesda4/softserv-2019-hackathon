# Generated by Django 2.2.6 on 2019-10-26 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='photo_path',
            field=models.CharField(max_length=255, null=True),
        ),
    ]

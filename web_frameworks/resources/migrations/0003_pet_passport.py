# Generated by Django 3.1.3 on 2020-11-10 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0002_auto_20201110_1638'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='passport',
            field=models.FileField(default='', upload_to='documents'),
            preserve_default=False,
        ),
    ]

# Generated by Django 2.1.1 on 2018-09-23 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20180923_0322'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='state',
            field=models.CharField(default='pending', max_length=100),
            preserve_default=False,
        ),
    ]

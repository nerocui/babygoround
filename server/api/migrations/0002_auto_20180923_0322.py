# Generated by Django 2.1.1 on 2018-09-23 03:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='client',
            name='api_client_name_8b2a0d_idx',
        ),
        migrations.AlterUniqueTogether(
            name='client',
            unique_together={('name', 'date_of_birth', 'baby_date_of_birth')},
        ),
    ]
# Generated by Django 4.0.1 on 2022-02-12 20:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0003_comment_text'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='post',
            table='portal_post',
        ),
    ]

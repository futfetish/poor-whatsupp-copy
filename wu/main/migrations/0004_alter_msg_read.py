# Generated by Django 4.2.1 on 2023-05-22 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_msg_read'),
    ]

    operations = [
        migrations.AlterField(
            model_name='msg',
            name='read',
            field=models.BooleanField(default=False),
        ),
    ]

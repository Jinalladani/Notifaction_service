# Generated by Django 4.0.4 on 2022-04-19 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_alter_notification_regdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='RegDate',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]

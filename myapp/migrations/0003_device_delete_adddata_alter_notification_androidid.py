# Generated by Django 4.0.4 on 2022-04-14 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_adddata'),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dname', models.CharField(blank=True, max_length=30, null=True)),
                ('androidid', models.CharField(blank=True, max_length=40, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='AddData',
        ),
        migrations.AlterField(
            model_name='notification',
            name='androidid',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]

# Generated by Django 5.1.4 on 2024-12-23 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]

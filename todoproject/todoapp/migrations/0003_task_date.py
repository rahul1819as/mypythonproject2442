# Generated by Django 4.2.4 on 2023-10-03 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_task_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='2000-02-03'),
            preserve_default=False,
        ),
    ]

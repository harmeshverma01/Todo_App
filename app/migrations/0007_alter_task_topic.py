# Generated by Django 4.1 on 2022-08-08 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_task_topic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='topic',
            field=models.CharField(default=True, max_length=50, null=True),
        ),
    ]

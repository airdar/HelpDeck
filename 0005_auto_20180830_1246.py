# Generated by Django 2.1 on 2018-08-30 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SupApp', '0004_auto_20180828_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='ReportTask',
            field=models.TextField(blank=True, null=True, verbose_name='Отчет выполнения задачи'),
        ),
    ]

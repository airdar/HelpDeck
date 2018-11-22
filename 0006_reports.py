# Generated by Django 2.1 on 2018-09-30 16:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SupApp', '0005_auto_20180830_1246'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reports',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Report', models.TextField(verbose_name='Отчет')),
                ('NameTask', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='SupApp.Task')),
            ],
        ),
    ]

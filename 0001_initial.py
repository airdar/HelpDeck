# Generated by Django 2.1 on 2018-08-23 14:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StatusTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NameStatus', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DateTimeTask', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания заявки')),
                ('AuthorTask', models.CharField(max_length=70, verbose_name='Автор заявки')),
                ('NameTask', models.CharField(max_length=80, verbose_name='Название задачи')),
                ('DescriptionTask', models.TextField(verbose_name='Описание задачи')),
                ('FlagTask', models.BooleanField(verbose_name='На контроле')),
                ('ReportTask', models.TextField(default='Не выполнено', verbose_name='Отчет выполнения задачи')),
                ('StatusTask', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='SupApp.StatusTask')),
                ('TaskExecutor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Исполнитель задачи')),
            ],
        ),
    ]

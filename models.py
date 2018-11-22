from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class StatusTask(models.Model):
    NameStatus = models.CharField(max_length=20)

    def __str__(self):
        return self.NameStatus


class Task (models.Model):
    DateTimeTask = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания заявки')
    AuthorTask = models.CharField(max_length=70, verbose_name='Автор заявки')
    NameTask = models.CharField(max_length=80, verbose_name='Название задачи')
    DescriptionTask = models.TextField(verbose_name='Описание задачи')
    NumberRoom = models.IntegerField(verbose_name='Номер комнаты')
    NumberComputer = models.IntegerField(verbose_name='Номер компьютера')
    StatusTask = models.ForeignKey(StatusTask, on_delete=models.CASCADE, default=1)
    FlagTask = models.BooleanField(verbose_name='На контроле', default=False)
    TaskExecutor = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Исполнитель задачи',default=1)
    ReportTask = models.TextField(verbose_name='Отчет выполнения задачи', null=True, blank=True)

    def __str__(self):
        return self.NameTask


class Reports (models.Model):
    NameTask = models.OneToOneField(Task,on_delete=models.CASCADE)
    Report = models.TextField(verbose_name= 'Отчет')

    def __str__(self):
        return self.Report
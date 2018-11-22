from .models import Task, Reports
from django.forms import ModelForm


class AddTaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['StatusTask','TaskExecutor','AuthorTask', 'NameTask', 'DescriptionTask', 'NumberRoom', 'NumberComputer','FlagTask']
        exclude = ('StatusTask','TaskExecutor','FlagTask', 'ReportTask')


class ReportForm(ModelForm):
    class Meta:
        model = Reports
        fields = ['NameTask', 'Report']
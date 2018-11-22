from django.contrib import admin
from .models import StatusTask, Task, Reports

# Register your models here.
admin.site.register(StatusTask)
admin.site.register(Task)
admin.site.register(Reports)
from django.db import models

'''
Task model consists of name of the task , detail explanation & Status of the Task
'''
class Task(models.Model):
    name=models.CharField(max_length=150)
    detail=models.TextField(max_length=255)
    completed=models.BooleanField(default=False)

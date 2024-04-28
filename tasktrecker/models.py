from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    completed = models.BooleanField(default=False, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    deadline_date = models.DateField(null=True, blank=True)
    dedline_time = models.TimeField(null=True, blank=True)
    user_id = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        return self.title
    
class TaskList(models.Model):
    user_id = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='tasklist')
    task_id = models.ForeignKey('Task', on_delete=models.CASCADE, related_name='tasklist')


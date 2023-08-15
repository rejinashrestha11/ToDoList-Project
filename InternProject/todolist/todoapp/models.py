from django.db import models

# Create your models here.

class Todolist(models.Model):
    task = models.CharField(max_length=120)
    description = models.TextField()
    due_date = models.DateField()
    completed = models.BooleanField(default=False)

    def _str_(self):
        return self.title
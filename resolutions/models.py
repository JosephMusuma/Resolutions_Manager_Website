from django.db import models
from django.contrib.auth.models import User

class Resolution(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateField()
    total_steps = models.IntegerField(default=100)  
    completed_steps = models.IntegerField(default=0)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
    def progress_percentage(self):
        if self.total_steps == 0:
            return 0
        return (self.completed_steps / self.total_steps) * 100

class Recommendation(models.Model):
    resolution = models.ForeignKey(Resolution, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.text[:50]
    

    def __str__(self):
        return self.user.username
    
class Progress(models.Model):
    resolution = models.ForeignKey(Resolution, on_delete=models.CASCADE)
    date = models.DateField()
    progress = models.TextField()

    def __str__(self):
        return f"{self.resolution.title} - {self.date}"
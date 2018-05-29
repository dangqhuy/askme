from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    answerer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="questions")
    content = models.CharField(max_length=250)
    answer = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.content
    




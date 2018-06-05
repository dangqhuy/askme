from django.db import models
from askmeV2.models import BaseModel
from django.contrib.auth.models import User


class Question(BaseModel):
    content = models.CharField(max_length=250)
    answer = models.TextField("answer", blank=True, null=True)
    answerer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="questions"
    )

    def __str__(self):
        return self.content

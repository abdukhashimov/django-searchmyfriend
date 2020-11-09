from django.db import models
from user.models import User
    
ANSWERS = (
    ("1","Strongly Disagree"),
    ("2","Disagree"),
    ("3","Neutral"),
    ("4","Agree"),
    ("5","Strongly Agree")
    ) 

class Question(models.Model):
    question_title = models.CharField(max_length=100)
    def __str__(self):
        return self.question_title



class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=100,choices=ANSWERS)
    user = models.ForeignKey(User, related_name='answers', on_delete=models.CASCADE,null=True)


    def __str__(self):
        return f'{dict(ANSWERS)[self.answer]} - {self.user} - {self.question}'





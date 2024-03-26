from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo (models.Model):
  no = models.AutoField(primary_key=True,auto_created=True)
  title = models.CharField(max_length=100)
  date = models.DateField(auto_now_add=True)
  is_done = models.BooleanField(default=False)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  
  def __str__(self):
    return self.title
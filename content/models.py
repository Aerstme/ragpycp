from django.db import models

# Create your models here.
from users.models import Login


class Post(models.Model):
    class Post(models.Model):
        created_by = models.ForeignKey(Login, on_delete=models.CASCADE)
        created_at = models.DateTimeField('Creation date', auto_now=True)
        body = models.CharField(max_length=1024, null=False, default=None, verbose_name='Content')
from django.db import models

class User(models.Model):
    userId = models.AutoField(primary_key=True)
    username = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    phone = models.JSONField()
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.username
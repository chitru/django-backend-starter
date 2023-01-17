from django.db import models

class User(models.Model):
    firstname = models.TextField(max_length=20)
    lastname = models.TextField(max_length=20)

    def __str__(self):
        return(self.firstname)

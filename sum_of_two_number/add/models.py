from django.db import models

# Create your models here.
class Operation(models.Model):
    number_one = models.IntegerField()
    number_two = models.IntegerField()
    result = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.number_one} + {self.number_two} = {self.result}"
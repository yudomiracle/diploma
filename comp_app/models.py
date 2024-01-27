from django.db import models


class Computer(models.Model):
    title = models.CharField(max_length=50)
    info = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='photos/')

    def __str__(self):
        return f'{self.title} - {self.price}'
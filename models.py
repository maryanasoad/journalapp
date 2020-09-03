from django.db import models


class Resource(models.Model):
    name = models.CharField(max_length=100)
    link = models.URLField()

    def __str__(self):
        return self.name

    def __str__(self):
        return self.link


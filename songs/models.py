from django.db import models


# Write your models here
class Performer(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Song(models.Model):
    # created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    length = models.IntegerField()
    performer = models.ForeignKey(Performer)

    class Meta:
        ordering = ['title',]

    def __str__(self):
        return self.title + ' by ' + self.artist

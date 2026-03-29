from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)  # Link to live site or GitHub
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
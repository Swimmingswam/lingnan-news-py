from django.db import models

# Create your models here.
class News(models.Model):
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = 'News'
    def __str__(self):
        return self.text
class NewsImage(models.Model):
    news = models.ForeignKey(News,1)
    iurl = models.CharField(max_length=1000)
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.iurl
class Image(models.Model):
    url = models.CharField(max_length=1000)
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.url
class Comment(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.text
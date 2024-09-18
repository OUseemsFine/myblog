from django.db import models
from django.urls import reverse
from django.db.models import UniqueConstraint # Constrains fields to unique values
from django.db.models.functions import Lower # Returns lower cased value of field
# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=300,help_text="This is the title of a blog")
    create_date = models.DateField()
    update_date = models.DateField()
    abstract = models.TextField(help_text="the abstract of this blog")
    content = models.TextField(help_text="the content of the blog")
    GENRE = (
        ('d', 'Diary'),
        ('s', 'Summary'),
        ('R', 'Review'),
    )

    genre = models.CharField(
        max_length=1,
        choices=GENRE,
        blank=True,
        default='d',
        help_text='Blog genre',
    )
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog-detail',args=[str(self.id)])
    
    def get_genre(self):
        GENRE = (
        ('d', 'Diary'),
        ('s', 'Summary'),
        ('R', 'Review'),
    )
        for item in GENRE:
            if item[0] == self.genre:
               return item[1]
      

class News(models.Model):
    '''News about the recent changes of the website'''
    update_date = models.DateField()
    content = models.TextField(help_text="the content of this news")
    
    def __str__(self):
        return str(self.update_date)
    
from django.db import models

# Create your models here.
class Post(models.Model):
    '''
    this is aclass to difine posts for blog
    '''

    author = models.CharField(User, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=250)
    content = models.TextField()
    category = models.CharField('Category', on_delete=models.SET_NULL, null=True)
    status = models.CharField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField()

    def __str__(self):
        return self.title

class Category(models.Model):
    '''
    this is a class to define categories for blog
    '''

    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name
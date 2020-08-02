from django.db import models
# Create your models here.

#1
#E
#dfaateadddafst
#ffd

class Book(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField( max_length=50,blank=True,null=True)
    ISBN = models.CharField(max_length=20,blank=True,null=True)
    
    def __str__(self):
        return self.name

class BookMemo(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    book = models.ForeignKey(Book,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

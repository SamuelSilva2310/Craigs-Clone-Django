from django.db import models

# Create your models here.

#Create the Search Model, (A database Module)
#It Will Grab the input and use it 
class Search(models.Model):
    search = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} - {}'.format(self.search, self.created)
   #So the Plurar is Correct (not searchs) 
    class Meta:
        verbose_name_plural = 'Searches'

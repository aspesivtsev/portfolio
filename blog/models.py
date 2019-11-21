from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    mod_date = models.DateTimeField(auto_now=True)
    body = models.TextField()
    image = models.ImageField(upload_to='images/blog/', blank=True)

    def __str__(self):
        return self.title

    def summary(self):
        '''This is shortening of the body text, like a preview'''
        return " ".join(self.body.split()[:20])+"..."
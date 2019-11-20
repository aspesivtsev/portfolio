from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/blog/', blank=True)

    def summary(self):
        '''This is shortening of the body text, like a preview'''
        return " ".join(self.body.split()[:20])+"..."
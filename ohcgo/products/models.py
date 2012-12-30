from django.db import models

class Product(models.Model):
    """
    A product made/offered by OHC
    """
    name           = models.CharField(max_length=200)
    description    = models.TextField()
    image_location = models.CharField(max_length=200)
    tracker        = models.URLField(blank=True, null=True)
    

    def __unicode__(self):
        return self.name

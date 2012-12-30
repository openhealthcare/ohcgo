from django.db import models

class Product(models.Model):
    """
    A product made/offered by OHC
    """
    name           = models.CharField(max_length=200)
    description    = models.TextField()
    image_location = models.CharField(max_length=200)
    tracker        = models.URLField(blank=True, null=True)

    # Links, instructions etc on how to get and use the app
    # get_the_app    = models.TextField()

    # eg 'Would you like to see an iPhone version of this app?'
    # question       = models.CharField(max_length=200)
    

    def __unicode__(self):
        return self.name

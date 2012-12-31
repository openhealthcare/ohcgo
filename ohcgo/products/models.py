from django.db import models

class Product(models.Model):
    """
    A product made/offered by OHC
    """
    _getapp_help = "Links, instructions etc on how to get and use the app"
    _question_help = "eg 'Would you like to see an iPhone version of this app?'"

    name           = models.CharField(max_length=200)
    description    = models.TextField()
    image_location = models.CharField(max_length=200)
    tracker        = models.URLField(blank=True, null=True)
    get_the_app    = models.TextField(blank=True, null=True, help_text=_getapp_help)
    question       = models.CharField(max_length=200, blank=True, null=True,
                                      help_text=_question_help)


    def __unicode__(self):
        return self.name

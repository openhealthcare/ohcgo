from django.db import models
from django.core.urlresolvers import reverse

class Product(models.Model):
    """
    A product made/offered by OHC
    """
    INSIGHT = 'in'
    DOCTORS = 'do'
    CATEGORY_CHOICES = (
        (INSIGHT, 'Tools for Insight'),
        (DOCTORS, 'Tools for Doctors')
        )

    _getapp_help = "Links, instructions etc on how to get and use the app"
    _question_help = "eg 'Would you like to see an iPhone version of this app?'"

    name           = models.CharField(max_length=200)
    description    = models.TextField()
    image_location = models.CharField(max_length=200)
    tracker        = models.URLField(blank=True, null=True)
    source         = models.URLField(blank=True, null=True)
    get_the_app    = models.TextField(blank=True, null=True, help_text=_getapp_help)
    question       = models.CharField(max_length=200, blank=True, null=True,
                                      help_text=_question_help)
    category       = models.CharField(max_length=2, choices=CATEGORY_CHOICES,
                                      blank=True, null=True)
    featured       = models.BooleanField(default=False)
    frontpage      = models.BooleanField(default=False)


    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tool_detail', kwargs={'pk': self.pk})

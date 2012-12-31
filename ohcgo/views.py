"""
Base Views for the OHC Django site
"""
from django.views.generic import TemplateView

from ohcgo.products.models import Product

class Home(TemplateView):
    """
    Render to our home.html templte after grabbing some
    extra context.
    """
    template_name = 'home.html'

    def get_context_data(self, **kw):
        """
        Return a dictionary of context data to use in our
        template.

        Return: {,}
        Exceptions: None
        """
        context = super(Home, self).get_context_data(**kw)
        context['products'] = Product.objects.all()
        return context

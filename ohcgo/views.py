"""
Base Views for the OHC Django site
"""
from django.views.generic import TemplateView

from ohcgo import feeds
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
        context['products'] = Product.objects.filter(frontpage=True)
        context['entries'] = feeds.recent_posts()
        try:
            context['featured'] = Product.objects.filter(featured=True)[0]
        except IndexError:
            if len(context['products']) < 1:
                context['featured'] = []
            else:
                context['featured'] = context['products'][0]
        return context

class Tools(TemplateView):
    """
    Render to our tools.html templte after grabbing some
    extra context.
    """
    template_name = 'tools.html'

    def get_context_data(self, **kw):
        """
        Return a dictionary of context data to use in our
        template.

        Return: {,}
        Exceptions: None
        """
        context = super(Tools, self).get_context_data(**kw)
        context['insight'] = Product.objects.filter(category=Product.INSIGHT)
        context['doctors'] = Product.objects.filter(category=Product.DOCTORS)
        return context

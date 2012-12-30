from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView, DetailView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from ohcgo.products.models import Product

urlpatterns = patterns(
    '',
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'projects-and-products^$', TemplateView.as_view(template_name='products.html'),
        name='products'),
    url(r'^hack-days$', TemplateView.as_view(template_name='hackdays.html'), name='hackdays'),
    url(r'^consultancy$', TemplateView.as_view(template_name='consultancy.html'),
        name='consultancy'),

    url(r'^product/(?P<pk>\d+)/?$', DetailView.as_view(model=Product,
                                                       template_name="product_detail.html")),
    # Examples:
    # url(r'^$', 'ohcgo.views.home', name='home'),
    # url(r'^ohcgo/', include('ohcgo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^grappelli/', include('grappelli.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)




urlpatterns += staticfiles_urlpatterns()

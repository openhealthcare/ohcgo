"""
Root URLConf for OHC Website
"""
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView, DetailView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from ohcgo.views import Home, Tools
from ohcgo.products.models import Product

urlpatterns = patterns(
    '',
    url(r'^$', Home.as_view(), name='home'),
    url(r'^tools$', Tools.as_view(), name='products'),
    url(r'^hack-days$', TemplateView.as_view(template_name='hackdays.html'), name='hackdays'),
    url(r'^board$', TemplateView.as_view(template_name='board.html'),
        name='board'),

    url(r'^consultancy$', TemplateView.as_view(template_name='consultancy.html'),
        name='consultancy'),
    url(r'^about$', TemplateView.as_view(template_name='about.html'), name='about'),
    url(r'^who$', TemplateView.as_view(template_name='who.html'), name='who'),
    url(r'^tool/(?P<pk>\d+)/?$', DetailView.as_view(model=Product,
                                                       template_name="tool_detail.html"),
        name='tool_detail'),
    # Examples:
    # url(r'^$', 'ohcgo.views.home', name='home'),
    # url(r'^ohcgo/', include('ohcgo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', nclude('django.contrib.admindocs.urls')),
    (r'^grappelli/', include('grappelli.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)




urlpatterns += staticfiles_urlpatterns()

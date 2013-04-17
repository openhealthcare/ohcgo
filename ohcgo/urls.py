"""
Root URLConf for OHC Website
"""
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView, DetailView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from ohcgo.views import Home, Tools, ContactView
from ohcgo.products.models import Product

urlpatterns = patterns(
    '',
    url(r'^$', Home.as_view(), name='home'),
    url(r'^tools$', Tools.as_view(), name='products'),
    url(r'^hack-days$', TemplateView.as_view(template_name='hackdays.html'), name='hackdays'),
    url(r'^consultancy$', TemplateView.as_view(template_name='consultancy.html'),
        name='consultancy'),
    url(r'^about$', TemplateView.as_view(template_name='about.html'), name='about'),
    url(r'^who$', TemplateView.as_view(template_name='who.html'), name='who'),
    url(r'^tool/(?P<pk>\d+)/?$', DetailView.as_view(model=Product,
                                                       template_name="tool_detail.html"),
        name='tool_detail'),

    # Contact Form
    url(r'^contact/?$', ContactView.as_view(), name='contact'),
    url(r'^contact/ta$', TemplateView.as_view(template_name='contact_ta.html'),
        name='contact-ta'),


    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', nclude('django.contrib.admindocs.urls')),
    (r'^grappelli/', include('grappelli.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^justamin/', include(admin.site.urls)),


    # Blog
    url(r'^blog/', include('zinnia.urls')),
    url(r'^comments/', include('django.contrib.comments.urls')),

    url(r'^login/$', 'django_cas.views.login', name='login'),
    url(r'^accounts/login/$', 'django_cas.views.login'),
    url(r'^logout/$', 'django_cas.views.logout', name='logout'),
)




urlpatterns += staticfiles_urlpatterns()
urlpatterns += patterns('',
                        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
            }),
                        )

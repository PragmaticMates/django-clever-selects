from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from views import HomeView, SimpleChainView, MultipleChainView, \
    AjaxChainedNames, AjaxChainedCountries, AjaxChainedCities, AjaxChainedView

urlpatterns = patterns('',
    # Examples:
    url(r'^ajax/chained-view/$', AjaxChainedView.as_view(), name='ajax_chained_view'),
    url(r'^ajax/chained-names/$', AjaxChainedNames.as_view(), name='ajax_chained_names'),
    url(r'^ajax/chained-countries/$', AjaxChainedCountries.as_view(), name='ajax_chained_countries'),
    url(r'^ajax/chained-cities/$', AjaxChainedCities.as_view(), name='ajax_chained_cities'),

    url(r'^simple-chain/$', SimpleChainView.as_view(), name='simple_chain'),
    url(r'^multiple-chain/$', MultipleChainView.as_view(), name='multiple_chain'),
    url(r'^$', HomeView.as_view(), name='home'),

    # url(r'^example/', include('example.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)


from django.conf.urls import patterns, url

from views import HomeView, SimpleChainView, MultipleChainView, \
    AjaxChainedNames, AjaxChainedCountries, AjaxChainedCities

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    url(r'^ajax/chained-names/$', AjaxChainedNames.as_view(), name='ajax_chained_names'),
    url(r'^ajax/chained-countries/$', AjaxChainedCountries.as_view(), name='ajax_chained_countries'),
    url(r'^ajax/chained-cities/$', AjaxChainedCities.as_view(), name='ajax_chained_cities'),

    url(r'^simple-chain/$', SimpleChainView.as_view(), name='simple_chain'),
    url(r'^multiple-chain/$', MultipleChainView.as_view(), name='multiple_chain'),
    url(r'^$', HomeView.as_view(), name='home'),

    # url(r'^example/', include('example.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

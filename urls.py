from django.conf.urls.defaults import patterns, include, url

from views import displayPairStair

urlpatterns = patterns('',
    url(r'^pairStair/$', displayPairStair),
    # url(r'^pairStair2/', include('pairStair2.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

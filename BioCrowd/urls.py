from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'BioCrowd.views.home', name='home'),
    # url(r'^BioCrowd/', include('BioCrowd.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    
    (r'^login/', include('BioCrowd.apps.login.urls')),
    (r'^account/', include('BioCrowd.apps.registration.urls')),
    (r'^account/', include('BioCrowd.apps.accounts.urls')),
    (r'^jobs/', include('BioCrowd.apps.jobs.urls')),
    (r'', include('BioCrowd.apps.pages.urls')),
)

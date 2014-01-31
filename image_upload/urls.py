from django.conf.urls import patterns, include, url

from image.views import ImageView

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'', ImageView.as_view(), name='image'),
    # Examples:
    # url(r'^$', 'image_upload.views.home', name='home'),
    # url(r'^image_upload/', include('image_upload.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

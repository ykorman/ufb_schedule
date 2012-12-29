from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ufb_schedule.views.home', name='home'),
    # url(r'^ufb_schedule/', include('ufb_schedule.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # auth
    url(r'^schedule/login$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url(r'^schedule/logout$', 'django.contrib.auth.views.logout', {'template_name': 'logout.html'}),

    # schedule
    url(r'^schedule/my_schedule$', 'schedule.views.trainee_schedule'),
    # select workout
    url(r'^schedule/workout_select$', 'schedule.views.workout_select'),
    # workout register
    url(r'^schedule/workout_register$', 'schedule.views.workout_register'),
)

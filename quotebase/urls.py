from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.views import login, logout
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('quotebase.views',
    url(r'^login/$', 'login_user'),
    url(r'^quotes/$', 'main'),
    url(r'^quote/(?P<quote_id>\d+)/$', 'quote_detail'),
    url(r'^quote/new/$', 'new_quote'),
    url(r'^quote/(?P<quote_id>\d+)/edit/$', 'edit_quote'),
    # url(r'^quote/(?P<quote_id>\d+)/compare/$', 'compare_costs'),
    url(r'costs/$', 'main_costs'),
    url(r'^cost/new/$', 'new_cost'),
    url(r'^test/$', 'test'),
    # url(r'^quote/view/(?P<quote_id>\d+)$', 'view_quote'),
    # url(r'^cost/(?P<cost_id>\d+)$', 'edit_cost'),
    # url(r'^cost/view/(?P<cost_id>\d+)$', 'view_cost'),
    url(r'^reference/$', 'reference'),
    url(r'^logout/$', 'logout_user'),
)

# Admin Site views
urlpatterns += patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()

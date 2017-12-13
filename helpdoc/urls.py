from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'helpdoc'

urlpatterns = [
	url(r'^$',views.index, name='home'),
    url(r'^index/$', views.index, name='home'),
    url(r'^post/$',views.post, name='post'),
    url(r'^detail/(?P<name>[\w-]+)/$', views.detail,name='detail'),
    url(r'^creapost/(?P<name>[\w-]+)/$',views.creapost, name='creapost'),
    url(r'^edit/(?P<id>[0-9]{2})/$',views.editmain, name='editmain'),
    url(r'^editdetail/(?P<id>[0-9]{2})/$',views.editdetail, name='editdetail'),
    url(r'^issue/$',views.issue, name='issue'),
    url(r'^creaissue/$',views.creaissue, name='creaissue'),
    url(r'^admin_user/$',views.admin_user, name='admin_user'),
    url(r'^admin_register/$',views.admin_register, name='admin_register'),
    url(r'^logout/$',views.logout, name='logout'),
    url(r'^pi_index/$',views.pi_index, name='pi_index'),
    url(r'^report_category/$',views.report_category, name='report_category'),
    url(r'^creaissue/jsondata/$',views.jsondata, name='jsondata'),
    url(r'^issue/jsondata/$',views.jsondata, name='jsodata'),

    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
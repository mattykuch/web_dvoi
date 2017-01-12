from django.conf.urls import url
from . import views
#from django.contrib.auth.views import login
#from django.contrib.auth.views import logout
#from django.contrib.auth.views import logout_then_login

urlpatterns = [
	# previous login view
	# url(r'^login/$', views.user_login, name='login'),

    #login logout
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^logout-then-login/$', 'django.contrib.auth.views.logout_then_login', name='logout_then_login'),
    # change password urls
    url(r'^password-change/$', 'django.contrib.auth.views.password_change', name='password_change'),
    url(r'^password-change/done/$', 'django.contrib.auth.views.password_change_done', name='password_change_done'),

    ## restore password urls
    url(r'^password-reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
    url(r'^password-reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$', 'django.contrib.auth.views.password_reset_confirm', name='password_reset_confirm'),
    url(r'^password-reset/complete/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),
    #Register
    url(r'^register/$', views.register, name='register'),
    #Edit profile
    url(r'^edit/$', views.edit, name='edit'),

	# dashboard urls
	url(r'^$', views.dashboard, name='dashboard'),		

]
from django.conf.urls import include, url
from django.contrib import admin
from api.views import StringView

urlpatterns = [
    # Examples:
    # url(r'^$', 'drfsetup.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    # Your API End Point
    url(r'^api/$', StringView.as_view()),
]

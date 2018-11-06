from django.conf.urls import url, include
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static
from .views import UserDetailView, UserFollowView


urlpatterns = [

    # url(r'^admin/', admin.site.urls),
     url(r'^(?P<username>[\w.@+-]+)/$', UserDetailView.as_view(), name="detail"),
     url(r'^(?P<username>[\w.@+-]+)/follow/$', UserFollowView.as_view(), name="follow"),
    # url(r'^profiles/', include(("accounts.urls",'profiles' ), namespace='profiles')),
    # url(r'^api/tweets/', include(('tweets.api.urls', "tweets-api"), namespace="tweets-api")),

]

if settings.DEBUG:
    urlpatterns +=(static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))
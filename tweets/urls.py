from django.conf.urls import url
from .views import TweetCreateView,  TweetUpdateView, TweetDeleteView,  TweetListView,  TweetDetailView, RetweetView
from django.views.generic.base import RedirectView
from django.urls import path
urlpatterns = [
    url(r'^$', RedirectView.as_view(url="/")), #/tweets
    url(r'^search/$', TweetListView.as_view(), name="list"), #/tweets/search/
    url(r'^create/$',TweetCreateView.as_view() , name="create"),  #/tweets/create
    url(r'^(?P<pk>\d+)/$',TweetDetailView.as_view() , name="detail"),  #/tweets/1/
    url(r'^(?P<pk>\d+)/retweet/$',RetweetView.as_view(), name="retweet"),  # /tweets/1/retweet
    url(r'^(?P<pk>\d+)/update/$',TweetUpdateView.as_view() , name="update"),  #/tweets/1/update
    url(r'^(?P<pk>\d+)/delete/$',TweetDeleteView.as_view() , name="delete"),  #/tweets/1/delete

]


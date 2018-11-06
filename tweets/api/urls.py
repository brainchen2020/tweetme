from django.conf.urls import url
# from .views import TweetCreateView,  TweetUpdateView, TweetDeleteView,  TweetListView,  TweetDetailView
from django.views.generic.base import RedirectView
from .views import TweetListAPIView, TweetCreateAPIView, ReTweetAPIView, LikeToggleAPIView, TweetDetailAPIView
urlpatterns = [
    # url(r'^$', RedirectView.as_view(url="/")), #/tweet
    url(r'^$', TweetListAPIView.as_view(), name="list"), #  /api/tweets
    url(r'^create/$',TweetCreateAPIView.as_view() , name="create"),  #/tweet/create
    # url(r'^search/$',SearchTweetAPIView.as_view() , name="search"),  #/tweet/create
    url(r'^(?P<pk>\d+)/$',TweetDetailAPIView.as_view() , name="detail"),  #/tweet/create
    url(r'^(?P<pk>\d+)/like/$', LikeToggleAPIView.as_view() , name="like"),  #/tweet/1/
    url(r'^(?P<pk>\d+)/retweet/$', ReTweetAPIView.as_view() , name="detail"),  #/tweet/1/
    # url(r'^(?P<pk>\d+)/update/$',TweetUpdateView.as_view() , name="update"),  #/tweet/1/update
    # url(r'^(?P<pk>\d+)/delete/$',TweetDeleteView.as_view() , name="delete"),  #/tweet/1/delete

]


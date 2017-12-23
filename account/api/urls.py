from django.conf.urls import url
from django.views.generic.base import  RedirectView
from .views import  SepetAPIView

urlpatterns = [
    #
    # url(r'^$', RedirectView.as_view(url="/")),
    url(r'^$', SepetAPIView.as_view() , name='sepet-list'),
    # url(r'^create/$', TweetCreateAPIView.as_view() , name='create'),
    # url(r'^(?P<pk>\d+)/retweet$',RetweetAPIView.as_view() , name='retweetS'),
    # url(r'^create/$', TweetCreateView.as_view() , name='create'),
    # url(r'^(?P<pk>\d+)/$', TweetDetailView.as_view(), name='detail'),
    # url(r'^(?P<pk>\d+)/update/$', TweetUpdateView.as_view(), name='update'),
    # url(r'^(?P<pk>\d+)/delete/$', TweetDeleteView.as_view(), name='update'),
]

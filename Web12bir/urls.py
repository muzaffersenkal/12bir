"""Web12bir URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from field.views import IndexView,ListView,DetailView
from account.views import UserRegister,ProfileView,SepetView




urlpatterns = [
    url(r'^$',IndexView.as_view(),name="index"),
     url(r'^api/field/', include('field.api.urls', namespace="field-api")),
     url(r'^api/sepet/', include('account.api.urls', namespace="sepet-api")),
    url(r'^list/$',ListView.as_view(),name="list"),
    url(r'^sepetim/$',SepetView.as_view(),name="sepetim"),
    url(r'^accounts/profile$',ProfileView.as_view(),name="profile"),
    url(r'^register/$',UserRegister.as_view(),name="register"),
    url('accounts/', include('django.contrib.auth.urls')),
    url(r'^list/(?P<slug>[-\w]+)/$',DetailView.as_view(),name="detail"),
    url(r'^admin/', admin.site.urls),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


from django.conf.urls import include, url
from django.contrib import admin

from .views import home,signIn,signUp
from django.utils.translation import gettext_lazy as _
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^signIn/$',signIn,name="signIn"),
    url(r'^signUp/$',signUp,name="signUp"),
    url(r'^',home,name="home")
]
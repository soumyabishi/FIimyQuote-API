"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin

from backend.views import *

urlpatterns = [
#    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='home'),
    url(r'^api/get-dialogues/$', DialogueViewSet.as_view({'get': 'get_dialogues'})),
    url(r'^api/add-emotion/$', DialogueViewSet.as_view({'post': 'add_emoji'})),
    url(r'^api/remove-emotion/$', DialogueViewSet.as_view({'post': 'remove_emoji'})),
    url(r'^api/add-dialogue/$', DialogueViewSet.as_view({'post': 'add_dialogue'}))
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns.append(url(r'^__debug__/', include(debug_toolbar.urls)))

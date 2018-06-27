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
    url(r'^api/get-dialogue-by-id/$', DialogueViewSet.as_view({'get': 'get_dialogue'})),
    url(r'^api/add-emotion/$', DialogueViewSet.as_view({'post': 'add_emoji'})),
    url(r'^api/remove-emotion/$', DialogueViewSet.as_view({'post': 'remove_emoji'})),
    url(r'^api/get-tags/$', TagViewSet.as_view({'get': 'get_all_tags'})),
    url(r'^api/get-year-range/$', DialogueViewSet.as_view({'get': 'get_year_range'})),
    url(r'^api/search-movies-star/$', DialogueViewSet.as_view({'get': 'search_results'})),
    url(r'^api/fetch-counts/$', DialogueViewSet.as_view({'get': 'get_counts'})),
    url(r'^api/slack/$', DialogueSlackViewSet.as_view({'post': 'get_dialogue'})),
    url(r'^\.well-known/acme-challenge/iJWaUiJulIuA-b5RZgxdxuSl8AjrNH57GnEKJzf0d2Y$', https_view_1),
    url(r'^\.well-known/acme-challenge/KHbZ7N85wkULa9I997i886bGodd0jHfERLtHyNA0ObU$', https_view_2),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns.append(url(r'^__debug__/', include(debug_toolbar.urls)))

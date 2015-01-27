from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from userManager.views import *
from SMGIS.views import *
from secretary.views import *
from markPost.views import *
from friends.views import *
from userTrack.views import *

#admin
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
]

#user
urlpatterns += [
    #url(r'^user/', include(admin.site.urls)),
    url(r'^user/(?P<pk>[0-9]+)$', UserDetail.as_view()),
    url(r'^user/$', UserList.as_view()),
    url(r'^user/profile/$', HimSelfDatail.as_view()),
    url(r'^user/info/$', UserInformationDatail.as_view()),
]
#userTrack
urlpatterns += [
    url(r'^track/$', UserTrackView.as_view()),
]

#Todo: do my api-auth
#api-auth
urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]

#gis
urlpatterns += [
    url(r'^gis/(?P<position>[\d\s\.]+)$', ChinaCityQuery.as_view()),
]

#secretary
urlpatterns += [
    url(r'^hello/$', Hello.as_view()),
    url(r'^home/$', Home.as_view()),
]

#friends
urlpatterns += [
    #url(r'^user/friends$', UserFriendsList.as_view()),
    #url(r'^user/makefriend$', AskMakeFriend.as_view()),
]

#markPost
urlpatterns += [
    url(r'^markpost/$', MarkPostList.as_view()),
    url(r'^user/markpost/(?P<pk>[0-9]+)$', UesrAllMarkPost.as_view()),
    url(r'^markpost/(?P<position>[\d\s\.]+)$', AreaMarkPosts.as_view()),
    url(r'^markpost/pk/(?P<pk>[0-9]+)$', MarkPostDetail.as_view()),
]

#static
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
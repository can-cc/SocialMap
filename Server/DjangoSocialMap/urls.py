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
from BasicServices.views import *

#admin
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
]

#user
urlpatterns += [
    #url(r'^user/', include(admin.site.urls)),
    url(r'^api/user/(?P<pk>[0-9]+)$', UserDetail.as_view()),
    url(r'^api/user/$', UserList.as_view()),

    url(r'^api/user/profile/$', HimSelfDatail.as_view()),
    #get and post
    url(r'^api/user/info/$', UserInformationDatail.as_view()),

    url(r'^api/user/simple/(?P<pk>[0-9]+)$', SimpleUserInfoDetail.as_view()),
    #portrait
    url(r'^api/user/portrait/(?P<pk>[0-9]+)$', UserPortraitDetail.as_view()),
    url(r'^api/user/portrait/$', UserPortraitList.as_view()),

    url(r'^api/user/show/(?P<pk>[0-9]+)$', UserInfoShow.as_view()),
]
#userTrack
urlpatterns += [
    url(r'^api/track/$', UserTrackView.as_view()),
]

#Todo: do my api-auth
#api-auth
urlpatterns += [
    url(r'^api/api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]

#gis
urlpatterns += [
    url(r'^api/gis/city/(?P<position>[\d\s\.]+)$', ChinaCityQuery.as_view()),
]

#secretary
urlpatterns += [
    url(r'^api/hello/$', Hello.as_view()),
    url(r'^api/home/$', Home.as_view()),
    url(r'^api/hasinfo/$', HasInfo.as_view()),
]

#friends
urlpatterns += [
    #url(r'^user/friends$', UserFriendsList.as_view()),
    #url(r'^user/makefriend$', AskMakeFriend.as_view()),
    url(r'^api/user/follows/$', UserFollowsList.as_view()),
    url(r'^api/user/follows/(?P<pk>[0-9]+)$', UserFollowsDetail.as_view()),

    url(r'^api/user/followers/$', UserFollowersList.as_view()),
    url(r'^api/user/followers/(?P<pk>[0-9]+)$', UserFollowersDetail.as_view()),
]


#message
urlpatterns += [
    url(r'^api/message/send/$', SenderMessageList.as_view()),
]



#markPost
urlpatterns += [
    url(r'^api/markpost/$', MarkPostList.as_view()),
    url(r'^api/user/markpost/$', UesrAllMarkPost.as_view()),
    url(r'^api/markpost/(?P<position>[\d\s\.]+)$', AreaMarkBubblePosts.as_view()),
    url(r'^api/markpost/pk/(?P<pk>[0-9]+)$', MarkPostDetail.as_view()),

    url(r'^api/markpost/(?P<pk>[0-9]+)/comment/$', CommitList.as_view()),
    url(r'^api/markpost/comment/(?P<pk>[0-9]+)$', CommitDetail.as_view()),
]

#static
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
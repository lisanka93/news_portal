from django.urls import path
from .views import Posts, PostDetail, PostSearch, PostAdd, PostDelete, PostUpdate #, showresults #PostList, Posts ,


urlpatterns= [
    path("", Posts.as_view()),
    path("search", PostSearch.as_view()),
    path("add/", PostAdd.as_view(), name="add"),
    #path('add/<int:pk>', PostAdd.as_view(), name='update'),
    path('<int:pk>/edit', PostUpdate.as_view(), name='update'),
    path("<int:pk>/delete", PostDelete.as_view(), name="delete"),
    #path("", PostList.as_view()),
    path('<int:pk>', PostDetail.as_view(), name="post"),
    #path("", showresults),
]

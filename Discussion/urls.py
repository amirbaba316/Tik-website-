from django.urls import path ,re_path
from .views import DiscussionView,DiscussionDetailView,NewDiscussionView
urlpatterns = [
  re_path(r'^discuss/$',DiscussionView.as_view(),name='discussion'),
  re_path(r'^discuss/(?P<slug>\w+)/$',DiscussionDetailView.as_view(),name='discussion_detail'),
  re_path(r'^addthread/$',NewDiscussionView.as_view(),name='add_thread')
]

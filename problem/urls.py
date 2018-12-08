from django.urls import path ,re_path
from .views import ProblemCreate,ProblemList,ProblemDetail,About
urlpatterns=[

    re_path(r'^create/$',ProblemCreate.as_view(),name='post_problem'),
    re_path(r'^display/$',ProblemList.as_view(),name='problem_list'),
    re_path(r'^detail/(?P<slug>\w+)/$',ProblemDetail.as_view(),name='problem_detail'),
    re_path(r'^about/$',About.as_view(),name='about'),


]

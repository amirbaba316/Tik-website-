from django.urls import path,re_path
from .views import Login,Register,Logout,UserProfileView,ProfileUpdateView,PasswordUpdateView,ContactUsView

urlpatterns = [
    re_path(r'^register/$',Register.as_view(),name='register'),
    re_path(r'^login/$',Login.as_view(),name='login'),
    re_path(r'^logout/$',Logout.as_view(),name='logout'),
    re_path(r'^users/(?P<username>[\w-]+)/$',UserProfileView.as_view(),name='user_profile'),
    re_path(r'^profile_update/$',ProfileUpdateView.as_view(),name='update_profile'),
    re_path(r'^change_password/$',PasswordUpdateView.as_view(),name='update_password'),
    re_path(r'^contact/$',ContactUsView.as_view(),name="contact"),
]

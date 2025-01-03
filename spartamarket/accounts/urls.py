from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/<str:username>/',views.profile, name='profile'),
    path('profile/<str:username>/edit/',views.profile_edit, name='profile_edit'),
    path('follow/<str:username>/', views.follow, name='follow')
]

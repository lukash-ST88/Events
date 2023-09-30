from django.urls import path, include
from .views import RegisterUser, LoginUser, logout_user, user_profile, user_profile_event, add_user_to_event, remove_user_from_event, main

urlpatterns = [
    path('', main, name='home'),
    path('signup/', RegisterUser.as_view(), name='signup'),
    path('login/', LoginUser.as_view(), name='login_user'),
    path('logout/', logout_user, name='logout_user'),
    path('users/<int:user_id>/', user_profile, name='profile'),
    path('users/<int:user_id>/<int:event_id>', user_profile_event, name='profile_event'),
    path('add/<int:event_id>/', add_user_to_event, name='user_add'),
    path('remove/<int:event_id>/', remove_user_from_event, name='user_remove')
]

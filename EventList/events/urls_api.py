from django.urls import path, include
from .views_api import EventListCreateView, EventRetrieveDestroyView, AddUserToEvent, RemoveUserFromEvent

urlpatterns = [
    path('events/', EventListCreateView.as_view(), name='events'),
    path('events/<int:pk>/delete/', EventRetrieveDestroyView.as_view(), name='delete'),
    path('events/<int:pk>/add/', AddUserToEvent.as_view(), name='add'),
    path('events/<int:pk>/remove/', RemoveUserFromEvent.as_view(), name='remove'),
    path('auth/', include('rest_framework.urls')),
]

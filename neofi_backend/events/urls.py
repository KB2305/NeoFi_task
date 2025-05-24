from django.urls import path
from .views import RegisterView, EventListCreateView, EventDetailView, ShareEventView, EventHistoryView, EventRollbackView

urlpatterns = [
    path('auth/register', RegisterView.as_view(), name='register'),
    path('events', EventListCreateView.as_view(), name='event-list-create'),
    path('events/<uuid:pk>', EventDetailView.as_view(), name='event-detail'),
    path('events/<uuid:id>/share', ShareEventView.as_view(), name='event-share'),
    path('events/<uuid:id>/history', EventHistoryView.as_view(), name='event-history'),
    path('events/<uuid:id>/rollback/<uuid:versionId>', EventRollbackView.as_view(), name='event-rollback')
]
from django.urls import path

from . import views

app_name = "messaging"

urlpatterns = [
    path("", views.InboxListView.as_view(), name="inbox"),
    path("sent/", views.SentListView.as_view(), name="sent"),
    path("compose/", views.MessageCreateView.as_view(), name="compose"),
    path("<int:pk>/", views.MessageDetailView.as_view(), name="detail"),
]


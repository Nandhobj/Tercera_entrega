from django.urls import path

from . import views

app_name = "pages"

urlpatterns = [
    path("", views.PageListView.as_view(), name="page_list"),
    path("create/", views.PageCreateView.as_view(), name="page_create"),
    path("<int:pk>/", views.PageDetailView.as_view(), name="page_detail"),
    path("<int:pk>/update/", views.PageUpdateView.as_view(), name="page_update"),
    path("<int:pk>/delete/", views.PageDeleteView.as_view(), name="page_delete"),
]


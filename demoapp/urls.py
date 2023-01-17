from django.urls import path
from django.urls import re_path as url
from . import views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path("", views.index),
    # Class Based: ApiView
    # path("User/", views.UserList.as_view()),
    # path("User/<int:pk>/", views.UserDetail.as_view()),
    # Function Based
    # path("User/", views.UserView, name="User"),
    # path(
    #     "User/<int:bill_idx>/", views.SingleBill, name="single-bill"
    # ),
    # Generics
    path(
        "User-create/",
        views.UserCreate.as_view(),
        name="User-create",
    ),
    path(
        "User-list", views.UserList.as_view(), name="User-list"
    ),
    path(
        "User-list-create",
        views.UserListCreate.as_view(),
        name="User-list-create",
    ),
    path(
        "User-update/<int:pk>",
        views.UserUpdate.as_view(),
        name="User-update",
    ),
    path(
        "User-delete/<int:pk>",
        views.UserDelete.as_view(),
        name="User-delete",
    ),
]

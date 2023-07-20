from django.contrib.auth.views import LoginView
from django.urls import path


from .views import (
    get_cookie_view,
    set_cookie_view,
    set_session_view,
    get_session_view,
    MyLogoutView,
    # AboutMeView,
    RegisterView,
    FooBarView,
    about_me,
    UsersListView,
    UserDetailsView,
    AvatarUpdateView,
    HelloView,
    UserOrdersListView,
    OrdersDataExportView,
)

app_name = "myauth"

urlpatterns = [
    # path("login/", login_view, name="login"),
    path(
        "login/",
        LoginView.as_view(
            template_name="myauth/login.html",
            redirect_authenticated_user=True,
        ),
        name="login",
    ),
    path('hello/', HelloView.as_view(), name="hello"),
    # path("logout/", logout_view, name="logout"),
    path("logout/", MyLogoutView.as_view(), name="logout"),
    # path("about-me/", AboutMeView.as_view(), name="about-me"),
    path("register/", RegisterView.as_view(), name="register"),
    path("about-me/", about_me, name="about-me"),
    path("users/", UsersListView.as_view(), name="users_list"),
    path("users/<int:pk>/", UserDetailsView.as_view(), name="user_details"),
    path("users/<int:pk>/update/", AvatarUpdateView, name="avatar_update"),
    path("users/<int:user_id>/orders/", UserOrdersListView.as_view(), name="user_orders"),
    path("users/<int:user_id>/orders/export/", OrdersDataExportView.as_view(), name="orders_export"),

    path("cookie/get/", get_cookie_view, name="cookie-get"),
    path("cookie/set/", set_cookie_view, name="cookie-set"),

    path("session/set/", set_session_view, name="session-set"),
    path("session/get/", get_session_view, name="session-get"),

    path("foo-bar/", FooBarView.as_view(), name="foo-bar"),
]

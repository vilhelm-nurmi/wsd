from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup_view, name="signup"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('profile/<str:link>', views.profile, name="profile"),
    path('profile/<str:link>/verify/', views.verify_account, name="verify"),
    path('profile/<str:link>/resendemail/', views.resend_email, name="resend"),
    path('profile/<str:link>/add_email/', views.add_email, name="add_email"),
    path('profile/<str:link>/change_profile/', views.change_profile, name="change_profile"),
    path('change_password/', views.change_password, name="change_password"),
]

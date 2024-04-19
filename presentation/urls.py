from django.urls import path

from presentation.controllers.User.UserView import UserView


urlpatterns = [
    path("create-user", UserView.as_view()),
]
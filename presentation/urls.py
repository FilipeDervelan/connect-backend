from django.urls import path

from presentation.controllers.Function.FunctionView import FunctionView
from presentation.controllers.Ministry.MinistryView import MinistryView
from presentation.controllers.User.UserView import UserView


urlpatterns = [
    path("create-user", UserView.as_view()),
    path("delete-user/<int:id>", UserView.as_view()),

    path("create-function", FunctionView.as_view()),

    path("create-ministry", MinistryView.as_view()),
]
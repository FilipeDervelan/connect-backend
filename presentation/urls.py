from django.urls import path

from presentation.controllers.Function.AssignFunctionView import AssignFunctionView
from presentation.controllers.Function.CreateFunctionView import CreateFunctionView
from presentation.controllers.Function.UpdateFunctionView import UpdateFunctionView
from presentation.controllers.Ministry.AssignMinistryView import AssignMinistryView
from presentation.controllers.Ministry.CreateMinistryView import CreateMinistryView
from presentation.controllers.Ministry.DeleteMinistryView import DeleteMinistryView
from presentation.controllers.Ministry.ListMinistriesView import ListMinistriesView
from presentation.controllers.Ministry.UpdateMinistryView import UpdateMinistryView
from presentation.controllers.Scale.CreateScaleView import CreateScaleView
from presentation.controllers.Scale.ListScalesView import ListScalesView
from presentation.controllers.Unavailability.CreateUnavailabilityView import CreateUnavailabilityView
from presentation.controllers.User.CreateUserView import CreateUserView
from presentation.controllers.User.DeleteUserView import DeleteUserView
from presentation.controllers.User.EditUserView import EditUserView


urlpatterns = [
    path("create-user", CreateUserView.as_view()),
    path("edit-user/<int:id>", EditUserView.as_view()),
    path("delete-user/<int:id>", DeleteUserView.as_view()),

    path("create-function", CreateFunctionView.as_view()),
    path("update-function", UpdateFunctionView.as_view()),

    path("create-ministry", CreateMinistryView.as_view()),
    path("update-ministry/<int:id>", UpdateMinistryView.as_view()),
    path("delete-ministry/<int:id>", DeleteMinistryView.as_view()),
    path("list-ministries", ListMinistriesView.as_view()),

    path("create-scale", CreateScaleView.as_view()),
    path("list-scales", ListScalesView.as_view()),

    path("create-unavailability", CreateUnavailabilityView.as_view()),

    path("assign-ministry", AssignMinistryView.as_view()),
    path("assign-function", AssignFunctionView.as_view()),
]
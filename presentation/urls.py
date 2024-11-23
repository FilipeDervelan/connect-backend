from django.urls import path
from rest_framework_simplejwt import views as jwt_views


from presentation.controllers.Function.AssignFunctionView import AssignFunctionView
from presentation.controllers.Function.CreateFunctionView import CreateFunctionView
from presentation.controllers.Function.UpdateFunctionView import UpdateFunctionView
from presentation.controllers.Logout.logout_view import LogoutView
from presentation.controllers.Ministry.AssignMinistryView import AssignMinistryView
from presentation.controllers.Ministry.CreateMinistryView import CreateMinistryView
from presentation.controllers.Ministry.DeleteMinistryView import DeleteMinistryView
from presentation.controllers.Ministry.ListMinistriesView import ListMinistriesView
from presentation.controllers.Ministry.UpdateMinistryView import UpdateMinistryView
from presentation.controllers.Ministry.DeassignMinistryView import (
    DeassignMinistryView,
)
from presentation.controllers.Scale.CreateScaleView import CreateScaleView
from presentation.controllers.Scale.DeleteScaleView import DeleteScaleView
from presentation.controllers.Scale.ListScalesView import ListScalesView
from presentation.controllers.Scale.UpdateScaleView import UpdateScaleView
from presentation.controllers.Unavailability.CreateUnavailabilityView import (
    CreateUnavailabilityView,
)
from presentation.controllers.Unavailability.DeleteUnavailabilityView import (
    DeleteUnavailabilityView,
)
from presentation.controllers.Unavailability.ListUnavailabilitiesView import (
    ListUnavailabilitiesView,
)
from presentation.controllers.Unavailability.UpdateUnavailabilityView import (
    UpdateUnavailabilityView,
)
from presentation.controllers.User.DeleteUserView import DeleteUserView
from presentation.controllers.register_user.register_user_view import RegisterUserView


urlpatterns = [
    path("register/", RegisterUserView.as_view(), name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path(
        "token/",
        jwt_views.TokenObtainPairView.as_view(),
        name="token_obtain_pair",
    ),
    path(
        "token/refresh/",
        jwt_views.TokenRefreshView.as_view(),
        name="token_refresh",
    ),
    # path("edit-user/<int:id>", EditUserView.as_view()),
    path("delete-user/<int:id>", DeleteUserView.as_view()),
    path("create-function", CreateFunctionView.as_view()),
    path("update-function", UpdateFunctionView.as_view()),
    path("create-ministry", CreateMinistryView.as_view()),
    path("update-ministry/<int:id>", UpdateMinistryView.as_view()),
    path("delete-ministry/<int:id>", DeleteMinistryView.as_view()),
    path("list-ministries", ListMinistriesView.as_view()),
    path("create-scale", CreateScaleView.as_view()),
    path("list-scales", ListScalesView.as_view()),
    path("delete-scale/<int:id>", DeleteScaleView.as_view()),
    path("update-scale/<int:id>", UpdateScaleView.as_view()),
    path("create-unavailability", CreateUnavailabilityView.as_view()),
    path("list-unavailabilities", ListUnavailabilitiesView.as_view()),
    path("update-unavailability/<int:id>", UpdateUnavailabilityView.as_view()),
    path("assign-ministry", AssignMinistryView.as_view()),
    path("deassign-ministry", DeassignMinistryView.as_view()),
    path("assign-function", AssignFunctionView.as_view()),
    path("delete-unavailability/<int:id>", DeleteUnavailabilityView.as_view()),
]

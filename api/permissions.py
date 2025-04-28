from rest_framework.permissions import IsAuthenticated


class IsAuthenticatedUserApi(IsAuthenticated):
    """Permission to check if the user is authenticated and has API access."""

    def has_permission(self, request, view):  # noqa: ANN001, ANN201, ARG002
        return bool(request.user and request.user.is_authenticated and request.user.has_api)

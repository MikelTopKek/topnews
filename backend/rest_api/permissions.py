# pylint: disable=R0901, E1131
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.viewsets import ModelViewSet


class PermissionsMixin(ModelViewSet):

    permission_classes_by_action = {
        "default": [AllowAny | IsAdminUser],
        "destroy": [IsAdminUser],
        "perform_create": [IsAdminUser]
    }

    def get_permissions(self):
        try:
            # return permission_classes depending on `action`
            return [
                permission()
                for permission in self.permission_classes_by_action[self.action]
            ]
        except KeyError:
            # action is not set return default permission_classes
            return [
                permission()
                for permission in self.permission_classes_by_action["default"]
            ]


class PermissionsPostsMixin(PermissionsMixin):

    permission_classes_by_action = {
        "default": [AllowAny | IsAdminUser],
        "partial_update": [IsAuthenticated],
        "destroy": [IsAuthenticated],
        "perform_create": [IsAuthenticated]

    }


class PermissionsUsersMixin(PermissionsMixin):

    permission_classes_by_action = {
        "default": [AllowAny | IsAdminUser],
        "partial_update": [IsAuthenticated],
        "destroy": [IsAdminUser],
        "perform_create": [IsAdminUser]

    }


class IsSuperUser(IsAdminUser):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)

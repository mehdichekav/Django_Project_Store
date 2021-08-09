# from django.contrib.auth.models import User
# from rest_framework import permissions
#
#
# class IsOwnerPermission(permissions.BasePermission):
#
#     def has_permission(self, request, view):
#         # return super().has_permission(request, view)
#         return request.user == User.objects.get(pk=view.kwargs['id'])
#
#     def has_object_permission(self, request, view, obj):
#         return super().has_object_permission(request, view, obj)
#
#
# class IsSuperuserPermission(permissions.BasePermission):
#
#     def has_permission(self, request, view):
#         return super().has_permission(request, view)
#
#     def has_object_permission(self, request, view, obj):
#         # return super().has_object_permission(request, view, obj)
#         if request.method in permissions.SAFE_METHODS:
#             return True
#         return obj.user == request.user
#

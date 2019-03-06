from rest_framework.permissions import BasePermission

class IsReviewer(BasePermission):
  """
  Permission to allow owners only
  """
  def has_object_permission(self, request, view, obj):
    return obj.reviewer == request.user

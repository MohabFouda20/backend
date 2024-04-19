from .permissions import IsStaffEditor
from rest_framework import permissions

class StaffEditorPermissionMixin():
    permissions_classes = [permissions.AllowAny , IsStaffEditor]
    
    
class UserQuerySetMixin():
    user_field = 'user' 
    def get_queryset(self , *args, **kwargs):
        user = self.request.user
        lookup_data = {}
        lookup_data[self.user_field] = user
            

        qs  = super().get_queryset().filter( *args, **kwargs)
        if user.is_staff :
            return qs
        return qs.filter(**lookup_data)
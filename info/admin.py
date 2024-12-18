from django.contrib import admin
from .models import Employee, Department, Group, Position, AppRequests, Link

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
      model = Employee
      list_display = ('myid', 'nickname', 'lastname', 'email', 'position', 'group', 'department', 'livestatus', 'supervisor')
            
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
      model = Department
      list_display = ('title', 'code')   

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
      pass

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
      pass

@admin.register(AppRequests)
class AppRequestsAdmin(admin.ModelAdmin):
      pass

@admin.register(Link) 
class LinkAdmin(admin.ModelAdmin):
      list_display = ['displaytext', 'url', 'linktype', 'description']
      pass
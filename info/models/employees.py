from django.db import models
from django.db.models import Model

class Position(Model):
      name = models.CharField(max_length=256, null=False)
      
      
class Department(Model):
      title = models.CharField(max_length=128, null=False)
      code = models.CharField(max_length=3, null=False)
      
      
class Group(Model):
      name = models.CharField(max_length=32, null=False)
      

# Create your models here.
class Employee(Model):
      status = models.CharField(max_length=16, null=True)
      myid = models.CharField(max_length=32, null=False)
      firstname = models.CharField(max_length=45, null=False)
      lastname = models.CharField(max_length=45, null=False)
      nickname = models.CharField(max_length=45, null=True)
      hiredate = models.DateField(blank=True, null=True)
      email = models.CharField(max_length=65, null=True)
      officephone = models.CharField(max_length=16, null=True)
      birthdate = models.CharField(max_length=10, null=True)
      lunch = models.TimeField(null=True)
      initials = models.CharField(max_length=3, null=True)
      department = models.ForeignKey(Department, on_delete=models.RESTRICT, null=True, related_name='employee_department')
      supervisor = models.ForeignKey('Employee', on_delete=models.RESTRICT, null=True, related_name='employee_supervisor')
      position = models.ForeignKey('Position', on_delete=models.RESTRICT, null=True, related_name='employee_position')
      payroll = models.CharField(max_length=16, null=True)
      type = models.CharField(max_length=16, null=True)
      routingslip = models.BooleanField(null=True)
      receptionrole = models.CharField(max_length=8, null=True)
      alphabet = models.CharField(max_length=26, null=True)
      group = models.ForeignKey('Group', on_delete=models.RESTRICT, null=True, related_name='employee_group')
      createdate = models.DateTimeField(blank=True, null=True)
      modifydate = models.DateTimeField(blank=True, null=True)
      modifiedby = models.ForeignKey('Employee', on_delete=models.RESTRICT, null=True, related_name='employee_modifiedby')
      terminal = models.BooleanField()
      
      class Meta:
            ordering = ['lastname', 'firstname']
            
      def __str__(self):
            return f'{self.lastname}, {self.firstname}'      
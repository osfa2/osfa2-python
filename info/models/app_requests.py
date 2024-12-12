from django.db import models
from django.db.models import Model

class AppRequests(Model):
      number = models.IntegerField(null=False)
      requestdate = models.DateField(null=False)
      subject = models.CharField(null=False, max_length=256)
      
      REQUEST_STATUS = [
            (1, 'C'),
            (2, 'P'),
            (3, 'V'),
            (4, 'W')            
      ]
      status = models.IntegerField(choices=REQUEST_STATUS, blank=True, default=2)
      
      REQUEST_PRIORITIES = [
            (1, 'H'),
            (2, 'L'),
            (3, 'M')
      ]
      priority = models.IntegerField(choices=REQUEST_PRIORITIES, blank=True, default=2)
      
      REQUEST_SOURCES = [
            (1, 'Banner'),
            (2, 'BOR'),
            (3, 'CL'),
            (4, 'F&S'),
            (5, 'FED'),
            (6, 'OSFA'),
            (7, 'OTH'),
            (8, 'ST'),
            (9, 'UGA')
      ]      
      source = models.IntegerField(choices=REQUEST_SOURCES,blank=True, default=7)
      
      # program
      department = models.ForeignKey('Department', on_delete=models.RESTRICT, null=True, related_name='requests_department')
      deadline = models.CharField(null=True, max_length=32)
      comment = models.TextField(null=True)
      complete_date = models.DateField(null=True)
      delete_date = models.DateField(null=True)
      
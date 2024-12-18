from django.db import models
from django.db.models import Model

class Link(Model):
      displaytext = models.CharField(max_length=256, null=False)
      url = models.CharField(max_length=256, null=False)
      
      LINK_TYPE = [
            (0, 'Quick Link'),
            (1, 'Approved Software')
      ]
      linktype = models.IntegerField(
            choices=LINK_TYPE,
            blank=True,
            default=1         
      )
      description = models.TextField(null=True)
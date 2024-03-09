from django.db import models
from members_management.models import *

class Tenths(models.Model):
    primary_key = models.AutoField(primary_key=True)
    tenth_unique_id = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    tenth_amount = models.IntegerField(null=True, default=0)
    tenth_date = models.DateField(null=True, blank=True, max_length=9000)
    tenth_member = models.ForeignKey(ChurchMembers,related_name="tenth_members", on_delete=models.SET_NULL, null=True, blank=True)
    tenth_registered_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'church_tenths_tbl'
        ordering = ['-primary_key']
        verbose_name_plural = "TENTHS"
        db_table_comment = "Church Tenths"

    def __str__(self):
        return "{}-{}".format(self.tenth_member, self.tenth_amount) 



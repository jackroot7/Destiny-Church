import uuid
from django.db import models



class SundayServices(models.Model):
    primary_key = models.AutoField(primary_key=True)
    service_unique_id = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    service_name = models.CharField(default='Ibada ya Jumapili', max_length=9000)
    service_is_active = models.BooleanField(default=True)
    service_registered_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'sunday_service_name_tbl'
        ordering = ['-primary_key']
        verbose_name_plural = "SUNDAY SERIVCES"
        db_table_comment = "Cronjob based table for registrering sunday services"

    def __str__(self):
        return "{}".format(self.service_name) 


class ChurchSerives(models.Model):
    from members_management.models import ChurchMembers
    primary_key = models.AutoField(primary_key=True)
    serive_unique_id = models.UUIDField(editable=False, default=uuid.uuid4, unique=True)
    serive_name = models.CharField(max_length=90, blank=True, null=True)
    serive_members = models.ManyToManyField(ChurchMembers,related_name="serive_members", blank=True)
   
    class Meta:
        db_table = 'church_services'
        ordering = ['-primary_key']
        verbose_name_plural = "CHURCH SERIVCES"

    def __str__(self):
        return "{}".format(self.serive_name)


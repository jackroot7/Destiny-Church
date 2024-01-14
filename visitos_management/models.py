import uuid
from django.db import models
from management_panel.models import SundayServices
from utils.Enums import *




class ChurchVisitors(models.Model):
    primary_key = models.AutoField(primary_key=True)
    visitor_unique_id = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    visitor_photo = models.CharField(max_length=9000, null=True, blank=True)
    visitor_name = models.CharField(max_length=9000)
    visitor_gender = models.CharField(choices=GenderInum.choices(), max_length=9000)
    visitor_phone = models.CharField(max_length=9000)
    visitor_email = models.CharField(default="", null=True, blank=True, max_length=9000)
    visitor_resident_city = models.CharField(default="", null=True, blank=True, max_length=9000)
    visitor_resident_street = models.CharField(default="", null=True, blank=True, max_length=9000)
    visitor_visit_reasons = models.CharField(choices=VisitReasonsInum.choices(),default=VisitReasonsInum.VISITING, null=True, blank=True, max_length=9000)
    visitor_spiritual_asistance = models.CharField(choices=SpiritualAsistanceInum.choices(),default=SpiritualAsistanceInum.PRAYER, null=True, blank=True, max_length=9000)
    visitor_comments = models.CharField(default="", null=True, blank=True, max_length=9000)
    visitor_sunday_service = models.ForeignKey(SundayServices,related_name="visitor_sunday_service", on_delete=models.SET_NULL , null=True, blank=True)
    visitor_registered_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'church_visitors_tbl'
        ordering = ['-primary_key']
        verbose_name_plural = "VISITORS"
        db_table_comment = "Church Visitors"

    def __str__(self):
        return "{}-{}".format(self.visitor_name, self.visitor_registered_date) 



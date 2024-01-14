import uuid
from django.db import models
from management_panel.models import SundayServices
from utils.Enums import *




class ChurchMembers(models.Model):
    primary_key = models.AutoField(primary_key=True)
    member_unique_id = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    member_name = models.CharField(max_length=9000)
    member_gender = models.CharField(choices=GenderInum.choices(), max_length=9000)
    member_phone = models.CharField(max_length=9000)
    member_email = models.CharField(default="", null=True, blank=True, max_length=9000)
    member_occupation = models.CharField(default="", null=True, blank=True, max_length=9000)
    member_resident_city = models.CharField(default="", null=True, blank=True, max_length=9000)
    member_resident_street = models.CharField(default="", null=True, blank=True, max_length=9000)
    member_maritual_status = models.CharField(choices=MaritualStatusInum.choices(),default=MaritualStatusInum.SINGLE, null=True, blank=True, max_length=9000)
    member_education_level = models.CharField(choices=EducationLevelInum.choices(), null=True, blank=True, max_length=9000)
    member_registered_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'church_members_tbl'
        ordering = ['-primary_key']
        verbose_name_plural = "MEMBERS"
        db_table_comment = "Church members"

    def __str__(self):
        return "{}-{}".format(self.member_name, self.member_registered_date) 



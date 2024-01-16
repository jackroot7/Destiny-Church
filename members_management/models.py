import uuid
from django.db import models
from utils.Enums import *




class ChurchMembers(models.Model):
    primary_key = models.AutoField(primary_key=True)
    member_unique_id = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    member_photo = models.CharField(max_length=9000, null=True, blank=True)
    member_name = models.CharField(max_length=9000)
    member_gender = models.CharField(choices=GenderInum.choices(), max_length=9000)
    member_phone = models.CharField(max_length=9000)
    member_email = models.CharField(default="", null=True, blank=True, max_length=9000)
    member_occupation = models.CharField(default="", null=True, blank=True, max_length=9000)
    member_resident_city = models.CharField(default="", null=True, blank=True, max_length=9000)
    member_resident_street = models.CharField(default="", null=True, blank=True, max_length=9000)
    member_maritual_status = models.CharField(choices=MaritualStatusInum.choices(),default=MaritualStatusInum.SINGLE, null=True, blank=True, max_length=9000)
    member_education_level = models.CharField(choices=EducationLevelInum.choices(), null=True, blank=True, max_length=9000)
    member_zone = models.ForeignKey('management_panel.ChurchZones',related_name="member_zones", on_delete=models.SET_NULL, null=True, blank=True)
    member_registered_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'church_members_tbl'
        ordering = ['-primary_key']
        verbose_name_plural = "MEMBERS"
        db_table_comment = "Church members"

    def __str__(self):
        return "{}-{}".format(self.member_name, self.member_registered_date) 




class ChurchChildren(models.Model):
    primary_key = models.AutoField(primary_key=True)
    child_unique_id = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    child_name = models.CharField(max_length=9000)
    child_age = models.IntegerField(max_length=9000)
    child_gender = models.CharField(choices=GenderInum.choices(), max_length=9000)
    child_resident_city = models.CharField(default="", null=True, blank=True, max_length=9000)
    child_resident_street = models.CharField(default="", null=True, blank=True, max_length=9000)
    child_zone = models.ForeignKey('management_panel.ChurchZones',related_name="child_zones", on_delete=models.SET_NULL, null=True, blank=True)
    child_registered_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'church_childrens_tbl'
        ordering = ['-primary_key']
        verbose_name_plural = "CHILDRENS"
        db_table_comment = "Church Childrens"

    def __str__(self):
        return "{}-{}".format(self.child_name, self.child_registered_date) 







import uuid
from django.db import models
from django.contrib.auth.models import User

RESPONSE_TYPE = [
    ("GAS_DEVICE", "GAS_DEVICE"),
    ("FUEL_DEVICE", "FUEL_DEVICE"),
]



class Sonsors(models.Model):
    primary_key = models.AutoField(primary_key=True)
    sensor_unique_id = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    sensor_name = models.CharField(default='', max_length=9000)
    serial_number = models.CharField(max_length=7, unique=True)
    sensor_type = models.CharField(default='', choices=RESPONSE_TYPE, max_length=9000, null=True)
    sensor_is_active = models.BooleanField(default=True)
    sensor_registered_by = models.ForeignKey(User, related_name="sensor_registered_by", on_delete=models.CASCADE, null=True)
    sensor_registered_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'fuel_sensors_tbl'
        ordering = ['-primary_key']
        verbose_name_plural = "Sensors"
        db_table_comment = "This Table Used to Store IOT Sensors for reading Fuel Levels"

    def __str__(self):
        return "{} - {}".format(self.sensor_name, self.serial_number) 



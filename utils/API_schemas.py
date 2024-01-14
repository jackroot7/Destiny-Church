import json
from ninja import NinjaAPI, Schema


class UsageInputSchema(Schema):
    gas_cylinder_iot_device: str 
    gas_cylinder_size_kg: float
    max_gas_level_mm: float
    gas_level_mm: float
    gas_level_percentage: float
    gas_threshold_level_mm: float
    gas_threshold_level_percentage: float
    tilt_angle: float
    gas_temp: float
    battery_level_percentage: float



class ConfigInputSchema(Schema):
    gas_cylinder_iot_device: str 



class Response(Schema):
    code: int
    success: bool
    message: str
    
    @classmethod
    def get_status_code(cls,id):
        try:
            file = open('assets/response_codes.json', 'r')
            file_codes = file.read()
            response_codes = json.loads(file_codes)

            response_code = next(code for code in response_codes if code["id"] == str(id))
            
            return Response(
                success = response_code['status'],
                code = response_code['code'],
                message = response_code['message']
            )
        
        except:
            return Response()
        

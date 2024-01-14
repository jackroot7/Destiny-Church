
from utils.Enums import *


class SysConfigs:
    def get_configs():
        return{
            'enums':{
                'genders': GenderInum.dict(),
                'reasons': VisitReasonsInum.dict(),
                'assistance': SpiritualAsistanceInum.dict(),
                'maritual': MaritualStatusInum.dict(),
                'education': EducationLevelInum.dict(),
                'sms_templates': SMSTemplateInum.dict(),
            }
        }
        
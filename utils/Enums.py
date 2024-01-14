import enum


class GenderInum(enum.Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"
    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]
    
    @classmethod
    def dict(cls):
        return [{"value":key.value, "name":key.name} for key in cls]


class VisitReasonsInum(enum.Enum):
    VISITING = "VISITING"
    JOINING = "JOINING"
    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]
    
    @classmethod
    def dict(cls):
        return [{"value":key.value, "name":key.name} for key in cls]


class SpiritualAsistanceInum(enum.Enum):
    PRAYER = "PRAYER"
    SALVATION = "SALVATION"
    COUNCELING = "COUNCELING"
    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]
    
    @classmethod
    def dict(cls):
        return [{"value":key.value, "name":key.name} for key in cls]


class MaritualStatusInum(enum.Enum):
    MARRIED = "MARRIED"
    WIDOW = "WIDOW"
    WIDOWER = "WIDOWER"
    SINGLE = "SINGLE"
    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]
    
    @classmethod
    def dict(cls):
        return [{"value":key.value, "name":key.name} for key in cls]


class EducationLevelInum(enum.Enum):
    NONE = "NONE"
    STANDARD_SEVEN = "STANDARD_SEVEN"
    FORM_IV = "FORM_IV"
    FORM_VI = "FORM_VI"
    DIPLOMA = "DIPLOMA"
    CERTIFICATE = "CERTIFICATE"
    DEGREE = "DEGREE"
    MASTERS = "MASTERS"
    PhD = "PhD"
    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]
    
    @classmethod
    def dict(cls):
        return [{"value":key.value, "name":key.name} for key in cls]


class SMSTemplateInum(enum.Enum):
    VISITORS = "VISITORS"
    PRAYERS = "PRAYERS"
    TENTHS = "TENTHS"
    GREETINGS = "GREETINGS"
    OTHER = "OTHER"
    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]
    
    @classmethod
    def dict(cls):
        return [{"value":key.value, "name":key.name} for key in cls]



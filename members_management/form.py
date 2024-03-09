from django import forms
from utils.Config import SysConfigs
from .models import ChurchMembers

class MemberForm(forms.ModelForm):
    class Meta:
        model = ChurchMembers
        fields = [
            'member_name', 'member_phone', 'member_gender', 'member_email', 
            'member_zone', 'member_maritual_status', 'member_education_level', 
            'member_resident_city', 'member_resident_street', 'member_occupation'
        ]
        widgets = {
            'member_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Member Full Name'}),
            'member_phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '255 xxx xxx xxx'}),
            'member_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'xxx@xxx.xxx'}),
            'member_resident_city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'eg. Dodoma'}),
            'member_resident_street': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'eg. Majengo'}),
            'member_occupation': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Member Occupation'}),
            'member_gender': forms.RadioSelect(choices=SysConfigs.get_configs()['enums']['genders']),
            'member_zone': forms.Select(),
            'member_maritual_status': forms.Select(choices=SysConfigs.get_configs()['enums']['maritual']),
            'member_education_level': forms.Select(choices=SysConfigs.get_configs()['enums']['education']),
        }

    # Example of dynamically populating the 'member_zone' field
    def __init__(self, *args, **kwargs):
        super(MemberForm, self).__init__(*args, **kwargs)
        # Assuming 'MemberZone' is a model containing zones
        self.fields['member_zone'].queryset = SysConfigs.get_configs()['enums']['zones']

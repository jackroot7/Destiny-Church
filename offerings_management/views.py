from django.shortcuts import redirect, render
from django.views import View
from members_management.models import ChurchMembers
from offerings_management.models import Tenths
from utils.Config import SysConfigs
from visitos_management.models import *


class OfferingsView(View):
    def get(self, request, **kwargs):
        if request.htmx:
            return render(request, 'views/offerings/offerings.html', {'visitors_list':"visitors_list",'config':SysConfigs.get_configs()} )
        else:
            return render(request, 'base_wraper.html', {'config':SysConfigs.get_configs(), 'visitors_list':"visitors_list",'template': 'views/offerings/offerings.html'} )


class TenthsManagementView(View):
    def get(self, request, **kwargs):
        members_list = ChurchMembers.objects.all()
        if request.htmx:
            return render(request, 'views/offerings/tenths.html', {'members_list': members_list,'config':SysConfigs.get_configs()} )
        else:
            return render(request, 'base_wraper.html', {'config':SysConfigs.get_configs(), 'members_list':members_list,'template': 'views/offerings/tenths.html'} )

    def post(self, request, **kwargs):
        new_tenth = Tenths.objects.create(**{field: request.POST.get(field) for field in ['tenth_date', 'tenth_amount']})
        new_tenth.tenth_member = ChurchMembers.objects.filter(member_unique_id = request.POST.get('tenth_member')).first()
        new_tenth.save()

        return redirect("tenths_list")


import threading
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from management_panel.models import ChurchZones

from utils.Config import SysConfigs
from utils.utils import get_message
from .models import *
from django.core.paginator import Paginator

class MembersView(View):
    def get(self, request, **kwargs):
        
        church_members_list = ChurchMembers.objects.all()

        paginator = Paginator(church_members_list, 5)
        church_members = paginator.page(1)
        
        members_list = {
            'title': "List of Church Members",
            'headers':['Name','Phone','Zone','Street','Maritual','Reg. Date', 'Action'],
            'has_action': True,
            'items':list(map(lambda  member: {
                "name":member[1].member_name,
                "phone":member[1].member_phone,
                "zone":"" if member[1].member_zone is None else member[1].member_zone.zone_name,
                "street":member[1].member_resident_street,
                "maritual":member[1].member_maritual_status,
                "date":member[1].member_registered_date.strftime("%d-%b-%Y"),
                'actions':[{'url':'members','method':'hx-delete','name': 'Delete','icon': 'trash','id':str(member[1].member_unique_id)}]
            }, enumerate(church_members, start=1))),
            
        }
       
        statistics = {
            "MALE": church_members_list.filter(member_gender = GenderInum.MALE.value).count(),
            "FEMALE": church_members_list.filter(member_gender = GenderInum.FEMALE.value).count(),
            "SINGLE": church_members_list.filter( member_maritual_status = MaritualStatusInum.SINGLE.value).count(),
            "MARRIED": church_members_list.filter( member_maritual_status = MaritualStatusInum.MARRIED.value).count(),
            "WIDOW": church_members_list.filter( member_maritual_status = MaritualStatusInum.WIDOW.value).count(),
            "WIDOWER": church_members_list.filter( member_maritual_status = MaritualStatusInum.WIDOWER.value).count(),
        }
        
        if request.htmx:
            return render(request, 'views/members/members_list.html', {"statistics":statistics,"pagenation":church_members,'members_list':members_list,'config':SysConfigs.get_configs()} )
        else:
            return render(request, 'base_wraper.html', {"statistics":statistics,"pagenation":church_members, 'config':SysConfigs.get_configs(), 'members_list':members_list,'template': 'views/members/members_list.html'} )


    def post(self, request, **kwargs):
        new_member = ChurchMembers.objects.create(**{k: request.POST.get(k) for k in ['member_name', 'member_phone', 'member_gender', 'member_email', 'member_maritual_status', 'member_education_level', 'member_resident_city', 'member_resident_street', 'member_occupation']})
        new_member.member_zone = ChurchZones.objects.filter(zone_unique_id = request.POST.get('member_zone')).first()
        new_member.save()

        return redirect("members")
    



    def delete(self, request, action_id, **kwargs):
        ChurchMembers.objects.filter(member_unique_id=action_id).delete()
        return HttpResponse("")




class ChildrensView(View):
    def get(self, request, **kwargs):
        
        curch_childs_list = ChurchChildren.objects.all()
        
        childs_list = {
            'title': "List of Church childs",
            'headers':['Name','Age','Zone','Street','Reg. Date'],
            'has_action': True,
            'items':list(map(lambda  child: {
                "name":child[1].child_name,
                "age":child[1].child_age,
                "zone":"" if child[1].child_zone is None else child[1].child_zone.zone_name,
                "street":child[1].child_resident_street,
                "date":child[1].child_registered_date.strftime("%d-%b-%Y"),
            }, enumerate(curch_childs_list, start=1))),
            
        }
        if request.htmx:
            return render(request, 'views/childs/childrens_list.html', {'childs_list':childs_list,'config':SysConfigs.get_configs()} )
        else:
            return render(request, 'base_wraper.html', {'config':SysConfigs.get_configs(), 'childs_list':childs_list,'template': 'views/childs/childrens_list.html'} )


    def post(self, request, **kwargs):
        new_child = ChurchChildren.objects.create(**{k: request.POST.get(k) for k in ['child_name', 'child_age', 'child_gender', 'child_resident_city', 'child_resident_street']})
        new_child.child_zone = ChurchZones.objects.filter(zone_unique_id = request.POST.get('child_zone')).first()
        new_child.save()

        return redirect("childrens")
    

    def delete(self, request, action_id, **kwargs):
        ChurchChildren.objects.filter(child_unique_id=action_id).delete()
        return HttpResponse("")







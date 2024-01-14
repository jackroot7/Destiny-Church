from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views import View

from utils.Config import SysConfigs
from .models import *

class VisitorsView(View):
    def get(self, request, **kwargs):
        
        users_list = ChurchVisitors.objects.all()
        
        users_list = {
            'title': "List of Church Visitors",
            'headers':['Name','Phone','City','Street','Assistance','Comments','Visit Date','Actions'],
            'has_action': True,
            'items':list(map(lambda  visitor: {
                "name":visitor[1].visitor_name,
                "phone":visitor[1].visitor_phone,
                "city":visitor[1].visitor_resident_city,
                "street":visitor[1].visitor_resident_street,
                "asistance":visitor[1].visitor_spiritual_asistance,
                "comments":"Hakuna" if visitor[1].visitor_comments is None else visitor[1].visitor_comments,
                "date":visitor[1].visitor_registered_date.strftime("%d-%b-%Y"),
                'actions':[{'url':'visitors','method':'hx-delete','name': 'Delete','icon': 'trash','id':str(visitor[1].visitor_unique_id)}]
            }, enumerate(users_list, start=1))),
            
        }

        if request.htmx:
            return render(request, 'views/visitors/visitors_list.html', {'users_list':users_list,'config':SysConfigs.get_configs()} )
        else:
            return render(request, 'base_wraper.html', {'config':SysConfigs.get_configs(), 'users_list':users_list,'template': 'views/visitors/visitors_list.html'} )


    def post(self, request, **kwargs):
        ChurchVisitors.objects.create(**{k: request.POST.get(k) for k in ['visitor_name', 'visitor_gender', 'visitor_phone', 'visitor_email', 'visitor_resident_city', 'visitor_resident_street', 'visitor_visit_reasons', 'visitor_spiritual_asistance', 'visitor_comments']})
        return redirect("visitors")
    

    def delete(self, request, action_id, **kwargs):
        ChurchVisitors.objects.filter(visitor_unique_id=action_id).delete()
        return HttpResponse("")
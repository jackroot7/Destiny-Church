import threading
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views import View
from management_panel.models import SMSTemplates

from utils.Config import SysConfigs
from utils.SMS_Notification import SMSMessage
from .models import *

class VisitorsView(View):
    def get(self, request, **kwargs):
        
        visitors_list = ChurchVisitors.objects.all()
        
        visitors_list = {
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
            }, enumerate(visitors_list, start=1))),
            
        }
        if request.htmx:
            return render(request, 'views/visitors/visitors_list.html', {'visitors_list':visitors_list,'config':SysConfigs.get_configs()} )
        else:
            return render(request, 'base_wraper.html', {'config':SysConfigs.get_configs(), 'visitors_list':visitors_list,'template': 'views/visitors/visitors_list.html'} )


    def post(self, request, **kwargs):
        print(request.POST)
        ChurchVisitors.objects.create(**{k: request.POST.get(k) for k in ['visitor_name', 'visitor_gender', 'visitor_phone', 'visitor_email', 'visitor_resident_city', 'visitor_resident_street', 'visitor_visit_reasons', 'visitor_spiritual_asistance', 'visitor_comments']})
        return redirect("visitors")
    

    def delete(self, request, action_id, **kwargs):
        ChurchVisitors.objects.filter(visitor_unique_id=action_id).delete()
        return HttpResponse("")


class VisitorsNotificationsView(View):
    def post(self, request, **kwargs):
        

        visitors_list = []
        if request.POST.get('visitor_group') == 'Week':
            visitors_list = ChurchVisitors.objects.filter(visitor_sunday_service__service_is_active = True).all()
        else:
            visitors_list = ChurchVisitors.objects.all()

        
        
        template = SMSTemplates.objects.filter(template_type=request.POST.get('sms_template'), template_is_active=True).first()

        for visitor in visitors_list:
            sms = template.template_descriptions.format(name=visitor.visitor_name, date=visitor.visitor_registered_date)
            sms_thred = threading.Thread(target=SMSMessage.send_message, args=(sms.replace('\n', '\n'), visitor.visitor_phone))
            sms_thred.start()
        
        return redirect("visitors")
    
    




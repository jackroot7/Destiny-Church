import time
from django.shortcuts import render

from utils.utils import get_message


# Create your views here.

def home(request):  
    get_message(request, 'You have successfully login', type="success")
    if request.htmx:
        return render(request, 'views/dashboard.html')
    else:
        return render(request, 'views/dashboard_full.html')

def forms(request):    
    if request.htmx:
        return render(request, 'views/forms.html')
    else:
        return render(request, 'views/forms_full.html')


def users_list(request):    
    users_list = {
        'title': "Customers List Table",
        'headers':['S.N','Name','Device Name','Created Date','Actions'],
        'has_action': True,
        'items':[
            {
            'sn': 1,
            'name': "John Doe",
            'device': "3259873259732",
            'date': "2015-09-21",
            'actions':{'Delete': 'trash', 'View': 'list-ul', 'Edit': 'edit-alt'}
            },{
                'sn': 2,
                'name': "Alexus Peterson",
                'device': "3259873259732",
                'date': "2015-09-21",
                'actions':{'Edit': 'edit-alt'}
            }
        ],
        
    }
    
    if request.htmx:
        return render(request, 'views/users.html', {'users_list':users_list} )
    else:
        return render(request, 'base_wraper.html', {'users_list':users_list,'template': 'views/users.html'} )

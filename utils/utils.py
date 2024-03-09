from datetime import datetime
from django.contrib import messages

def get_message(request, message, type = 'info', title="Notification")->messages:

    body = {"title": title, "message": message, "time": datetime.now()}

    if type == 'success':
        messageobj = messages.success(request,body)

    elif type == 'error':
        messageobj = messages.error(request,body)

    elif type == 'warning':
        messageobj = messages.warning(request,body)
    else:
        messageobj = messages.info(request,body)

    return messageobj
from django.contrib import messages

def get_message(request, message, type = 'info', title="Notification")->messages:

    body = {"message": message, }

    if type == 'success':
        message = messages.success(request,body)

    if type == 'error':
        message = messages.error(request,body)

    if type == 'warning':
        message = messages.warning(request,body)
    else:
        message = messages.info(request,body)
        
    return message
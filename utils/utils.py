from django.contrib import messages

def get_message(request, message, type = 'info', title="Notification")->messages:

    message = messages.info(request,message)

    return message
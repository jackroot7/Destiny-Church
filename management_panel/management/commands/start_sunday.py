from django.core.management.base import BaseCommand
from datetime import datetime
from management_panel.models import SundayServices

class Command(BaseCommand):
    help = 'This command create new financial year to the system at every 01 July'

    def handle(self, *args, **options):
        SundayServices.objects.filter(service_is_active=True).update(service_is_active=False)

        current_day = datetime.now().strftime("%d-%b-%Y")
        
        new_serive, _ = SundayServices.objects.update_or_create(
            service_name = str('Ibada ya Jumapili ya tarehe ')+str(current_day)
        )
        
        print("New Sunday Service: ", str(new_serive.service_name))

        self.stdout.write(self.style.SUCCESS('New Sunday Service created successfully.'))

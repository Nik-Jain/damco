from django.core.management import BaseCommand
from django.core.management.base import CommandParser
from typing import Any, Optional
from ...utilities.data_utility import *
from ...utilities.email_utility import *
from ...utilities import CONSTANT

class Command(BaseCommand):
    help = 'This is utility to import recipe data to django models'
    
    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('filepath', type=str, help='Excel file path')
        
        # Optional argument
        parser.add_argument('-s', '--server', type=str, help='Define a SMTP server')
        parser.add_argument('-p', '--port', type=str, help='Define a SMTP server port')
        parser.add_argument('-f', '--from', type=str, help='Sender email ID')
        parser.add_argument('-t', '--to', nargs='+', type=str, help='Receiver email ID')
    
    def handle(self, *args: Any, **kwargs: Any) -> Optional[str]:
        filepath = kwargs['filepath']
        server = kwargs['server'] or CONSTANT.SMTP_SERVER
        port = kwargs['port'] or CONSTANT.SMTP_PORT
        sender = kwargs['from'] or CONSTANT.SENDER
        receiver = kwargs['to'] or CONSTANT.RECEIVER
        success_count, failure_count = save_excel_data(filepath)
        self.stdout.write(f'success_count --> {success_count}')
        self.stdout.write(f'failure_count --> {failure_count}')
        if failure_count:
            send_failure_email(success_count, failure_count, filepath, server, port, sender, receiver)
        else:
            send_success_email(success_count, server, port, sender, receiver)
        
        # return super().handle(*args, **options)
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Displays hello.'

    def handle(self, *args, **kwargs):
        self.stdout.write("Hello")

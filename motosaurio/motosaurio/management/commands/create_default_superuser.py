from django.core.management.base import BaseCommand
from motosaurio.models import MiUsuario

class Command(BaseCommand):
    help = 'Create the default superuser'

    def handle(self, *args, **options):
        username = 'motosaurio'
        email = 'motosaurio_project_123@outlook.com'
        password = 'motosaurio_project_123'

        # Check if the user already exists
        if not MiUsuario.objects.filter(username=username).exists():
            MiUsuario.objects.create_superuser(username, email, password)
            self.stdout.write(self.style.SUCCESS(f'Successfully created superuser: {username}'))
        else:
            self.stdout.write(self.style.WARNING(f'Superuser {username} already exists'))

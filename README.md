# Custom Management Commands in Django.

Part of Code Band YouTube video.

## Usage

1) Basic Example
#### management/commands/hello.py

```python
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Displays hello.'

    def handle(self, *args, **kwargs):
        self.stdout.write("Hello")
```

2) Handling Arguments

### ```Positional Arguments```
#### management/commands/generate_users.py
```python
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string


class Command(BaseCommand):
    help = 'Generate random users'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Indicates the number of users to be created')

    def handle(self, *args, **kwargs):
        count = kwargs['count']
        for i in range(count):
            User.objects.create_user(username=get_random_string(), email='hello@hi.com', password='123')
```

### ```Optional Arguments```
#### management/commands/generate_users.py
```python
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string


class Command(BaseCommand):
    help = 'Generate random users'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Indicates the number of users to be created')

        # Optional argument
        parser.add_argument('-p', '--prefix', type=str, help='Define a username prefix')

    def handle(self, *args, **kwargs):
        count = kwargs['count']
        prefix = kwargs['prefix']

        for i in range(count):
            if prefix:
                username = f'{prefix}_{get_random_string()}'
            else:
                username = get_random_string()
            User.objects.create_user(username=username, email='hello@hi.com', password='123')
```

### ```Boolean/Flag arguments```
#### management/commands/generate_users.py
```python
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string


class Command(BaseCommand):
    help = 'Generate random users'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Indicates the number of users to be created')
        parser.add_argument('-p', '--prefix', type=str, help='Define a username prefix')
        parser.add_argument('-s', '--superuser', action='store_true', help='Create a superuser account')

    def handle(self, *args, **kwargs):
        count = kwargs['count']
        prefix = kwargs['prefix']
        superuser = kwargs['superuser']

        for i in range(count):
            if prefix:
                username = f'{prefix}_{get_random_string()}'
            else:
                username = get_random_string()

            if superuser:
                User.objects.create_superuser(username=username, email='hello@hi.com', password='123')
            else:
                User.objects.create_user(username=username, email='hello@hi.com', password='123')
```

### ```Arbitrary List of Arguments```
#### management/commands/remove_users.py
```python
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Remove users'

    def add_arguments(self, parser):
        parser.add_argument('user_id', nargs='+', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        users_ids = kwargs['user_id']

        for user_id in users_ids:
            try:
                user = User.objects.get(pk=user_id)
                user.delete()
                self.stdout.write(f'User {user.username} with id {user_id} removed successfully!')
            except User.DoesNotExist:
                self.stdout.write(f'User with id {user_id} does not exist.')

```

3) Styling

#### ```Success```
```python
self.stdout.write(self.style.SUCCESS(f'User {user.username} with id {user_id} removed successfully!'))
```
#### ``` Warning ```
```python
self.stdout.write(self.style.WARNING(f'User with id {user_id} does not exist.'))
```

Thank you for checking out.

Don't forget to drop a ⭐

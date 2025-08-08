# myapp/management/commands/repeat_model_object.py

from django.core.management.base import BaseCommand
from django.apps import apps
from django.core.exceptions import ObjectDoesNotExist

class Command(BaseCommand):
    help = 'Duplicates the first object of the specified model 10 times'

    def add_arguments(self, parser):
        # Argument to accept the model name
        parser.add_argument('model_name', type=str, help='Name of the model to duplicate the first object from')

    def handle(self, *args, **kwargs):
        # Get the model name from the command arguments
        model_name = kwargs['model_name']

        # Try to get the model dynamically from the provided name
        try:
            Model = apps.get_model('BhimmaviApp', model_name)  # Replace 'myapp' with your app name

            # Fetch the first object of the model
            first_object = Model.objects.first()

            if first_object:
                # Duplicate the first object 10 times
                for i in range(10):
                    first_object.pk = None  # Reset primary key to create a new instance
                    first_object.save()  # Save the duplicated object
                    self.stdout.write(self.style.SUCCESS(f'Duplicated object {i + 1}'))

                self.stdout.write(self.style.SUCCESS(f'Successfully duplicated the first object of {model_name} 10 times!'))

            else:
                self.stdout.write(self.style.WARNING(f'No objects found in the {model_name} model! Please create an object first.'))

        except LookupError:
            self.stdout.write(self.style.ERROR(f'Model "{model_name}" not found in your app. Make sure the model exists.'))

        except ObjectDoesNotExist:
            self.stdout.write(self.style.ERROR(f'Error occurred while trying to fetch the object from model "{model_name}".'))
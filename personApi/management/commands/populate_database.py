import csv

from django.core.management.base import BaseCommand

from personApi.models import Person


class Command(BaseCommand):
    help = 'Populates the database with data from a CSV file'

    def handle(self, *args, **options):
        csv_file = 'dataset1.txt'
        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                person = Person.objects.create(
                    category=row['category'],
                    firstname=row['firstname'],
                    lastname=row['lastname'],
                    email=row['email'],
                    gender=row['gender'],
                    birth_date=row['birth_date']
                )
                person.save()
        self.stdout.write(self.style.SUCCESS('Data imported successfully'))

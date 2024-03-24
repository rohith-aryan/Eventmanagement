# base/management/commands/populate_events.py

import csv
from datetime import datetime
from django.core.management.base import BaseCommand
from base.models import Event
import os

class Command(BaseCommand):
    help = 'Populate database with event data from CSV file'

    def handle(self, *args, **kwargs):
        csv_file_path = os.path.join(os.path.dirname(__file__), '..', '..', 'data.csv')
        
        with open(csv_file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                event_name = row['event_name']
                city_name = row['city_name']
                date = datetime.strptime(row['date'], '%Y-%m-%d')
                time = row['time']
                latitude = float(row['latitude'])
                longitude = float(row['longitude'])
                
                Event.objects.create(
                    event_name=event_name,
                    city_name=city_name,
                    date=date,
                    time=time,
                    latitude=latitude,
                    longitude=longitude
                )

        self.stdout.write(self.style.SUCCESS('Database populated successfully'))

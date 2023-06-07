import os 
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "league.settings")

import django 
django.setup() 

from faker import factory,Faker 
from league_api.models import * 
from model_bakery.recipe import Recipe,foreign_key 

fake = Faker() 

for k in range(16):
    team=Recipe(Team,
                name=fake.name(),
                abbr=fake.name(),)
    team.make();
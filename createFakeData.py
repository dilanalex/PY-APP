import os 
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "league.settings")

import django 
django.setup() 

from faker import factory,Faker 
from league_api.models import * 
from model_bakery.recipe import Recipe,foreign_key 

fake = Faker() 
rounds = ["QF", "SF", "FI", "WI"]

for k in range(16):
    team=Recipe(Team,
                name=fake.name(),
                abbr=fake.name(),)
    team.make();

for k in range(8):
    game=Recipe(Game,
                host=foreign_key(team),
                guest=foreign_key(team),
                host_score=fake.random_number(digits=5),
                guest_score=fake.random_number(digits=5),
                winner=foreign_key(team),
                date=fake.date(),
                round_number=fake.sentence(ext_word_list = rounds))
    game.make();
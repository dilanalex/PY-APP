import os

from django.shortcuts import get_object_or_404 
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

user_types = ['COACH', 'PLAYER', 'ADMIN']
for type in range(len(user_types)):
    role=Recipe(Role,
                type=user_types[type])
    role.make();

##User data migration
for k in range(100):
    username = fake.user_name()+str(k)
    password = 'league'

    user=Recipe(User,
                username=username,
                email=fake.safe_email(),
                password=password,
                first_name=fake.first_name,
                last_name=fake.last_name())
    user.make()

##User Role Data Migration
users = User.objects.filter(is_superuser=False)
player = get_object_or_404(Role, type='PLAYER')
coach = get_object_or_404(Role, type='COACH')
admin = get_object_or_404(Role, type='ADMIN')

for user in users[:100]:
    
    user_role=Recipe(User_Role,
                user_id=user.id,
                role_id=player.id)
    user_role.make()

##Coach data migration and matching
teams = Team.objects.all()
coach = Role.objects.filter(type='COACH').first()
users = User_Role.objects.filter(role_id=coach.id)

for k in range(len(teams)):
    
    coach=Recipe(Coach,
                team_id=teams[k].id,
                user_id=users[k].id)
    Coach.make()
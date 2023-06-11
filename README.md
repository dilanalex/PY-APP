<h1>Requirements</h1>

<ul>
  <li>A total of 16 teams played in the first qualifying round, 8 moved to the next round, and so forth until one team was crowned as champion.
</li>
  <li>Each team consists of a coach and 10 players. not all players participate in every 
game.
</li>
  <li>There are 3 types of users in the system - the league admin, a coach, and a player.</li>
  <li>All 3 types of users can login to the site and logout. Upon login they will view the scoreboard, which will display all games and final scores, and will reflect how the competition progressed and who won.</li>
  <li>A coach may select his team in order to view a list of the players on it, and the average score of the team. When one of the players in the list is selected, his personal details will be presented, including - player’s name, height, average score, and the number of games he participated in. 
</li>
  <li>A coach can filter players to see only the ones whose average score is in the 90 percentile across the team.
</li>
  <li>The league admin may view all teams details - their average scores, their list of players, and players details. 
</li>
  <li>The admin can also view the statistics of the site’s usage - number of times each user logged into the system, the total amount of time each user spent on the site, and who is currently online</li>
</ul>

<h1>Versions</h1>
python --version
Python 3.9.6 </br>

<h1>Some Importnant Commands</h1>
py -3 -m venv .venv

python manage.py createsuperuser  - created super user, root/root</br>

python manage.py migrate</br>
python manage.py makemigrations</br>

django-admin startproject league</br>
django-admin startapp league_api</br>

python manage.py runserver</br>

<h2>Fake Data Population References</br>
https://www.educative.io/courses/django-admin-web-developers/RLPEYWRpDPV

<h2>Run this command for the data migrations </br>
python createFakeData.py

<h1>Avaialble APIs</h1>

  api_test/ - Learning purposes
  scoreboard/ - Score Board of the League
  team/ - Get All Team Information
  team/<int:team_id>/ - Team by Specific Team ID
from django.shortcuts import render, redirect
from .models import League, Team, Player
from django.db.models import Count

from . import team_maker

def index(request):
	context = {
		"leagues": League.objects.all(),
		"teams": Team.objects.all(),
		"players": Player.objects.all(),
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")

def chapters(request):

	return render(request, "leagues/chapters.html")

####


def baseball_leagues(request):
	result=League.objects.filter(sport="Baseball")
	name=[]
	for league in result:
		name.append(league.name)
	context = {
		"title": "All Baseball Leagues",
		"results": name
	}
	return render(request, "leagues/results.html", context)


def all_women_leagues(request):
	result=League.objects.filter(name__contains="Womens")
	name=[]
	for league in result:
		name.append(league.name)
	context = {
		"title": "All Womens' Leagues",
		"results": name

	}
	return render(request, "leagues/results.html", context)



def all_leagues_hockey(request):
	result=League.objects.filter(sport__contains="Hockey")
	name=[]
	for league in result:
		name.append(league.name)
	context = {
		"title": "All Leagues where sport is any type of Hockey",
		"results": name
	}
	return render(request, "leagues/results.html", context)

def other_than_football(request):
	result=League.objects.exclude(sport="Football")
	name=[]
	for league in result:
		name.append(league.name)
	context = {
		"title": "All leagues where sport != Football",
		"results": name
	}
	return render(request, "leagues/results.html", context)

def all_conferences(request):
	result=League.objects.filter(name__contains="Conference")
	name=[]
	for league in result:
		name.append(league.name)
	context = {
		"title": "All leagues self-proclaimed as 'Conferences'",
		"results": name
	}
	return render(request, "leagues/results.html", context)


def atlantic_leagues(request):
	result=League.objects.filter(name__contains="Atlantic")
	name=[]
	for league in result:
		name.append(league.name)
	context = {
		"title": "All teams in the Atlantic Region",
		"results": name
	}
	return render(request, "leagues/results.html", context)


def teams_dallas(request):
	result=Team.objects.filter(location="Dallas")
	name=[]
	for team in result:
		name.append(team.team_name)
	context = {
		"title": "All Teams based in Dallas",
		"results": name
	}
	return render(request, "leagues/results.html", context)


def raptors(request):
	result=Team.objects.filter(team_name__contains="Raptors")
	name=[]
	for team in result:
		name.append(team.team_name)
	context = {
		"title": "All teams dubbed The Raptors",
		"results": name
	}
	return render(request, "leagues/results.html", context)


def all_city(request):
	result=Team.objects.filter(location__contains="City")
	name=[]
	for team in result:
		name.append(team.team_name)
	context = {
		"title": "All teams whose location includes keyword:City",
		"results": name
	}
	return render(request, "leagues/results.html", context)


def all_t(request):
	result=Team.objects.filter(team_name__startswith="T")
	name=[]
	for team in result:
		name.append(team.team_name)
	context = {
		"title": "All teams who's names start with T",
		"results": name
	}
	return render(request, "leagues/results.html", context)

####

def location_alpha(request):
	result=Team.objects.filter().order_by('location')
	name=[]
	for team in result:
		name.append(team.team_name)
	context = {
		"title": "All teams, ordered alphabetically by location",
		"results": name
	}
	return render(request, "leagues/results.html", context)


def team_reverse(request):
	result=Team.objects.filter().order_by('-team_name')
	name=[]
	for team in result:
		name.append(team.team_name)
	context = {
		"title": "All teams, ordered by reverse alphabetical order",
		"results": name
	}
	return render(request, "leagues/results.html", context)


def all_cooper(request):
	result=Player.objects.filter(last_name="Cooper")
	name=[]
	for player in result:
		name.append(player.first_name + " " + player.last_name)
	context = {
		"title": "All players who's last name is Cooper",
		"results": name
	}
	return render(request, "leagues/results.html", context)


def all_josh(request):
	result=Player.objects.filter(first_name="Joshua")
	name=[]
	for player in result:
		name.append(player.first_name + " " + player.last_name)
	context = {
		"title": "All players who's first name is Joshua",
		"results": name
	}
	return render(request, "leagues/results.html", context)


def except_josh(request):
	result=Player.objects.filter(last_name="Cooper").exclude(first_name="Joshua")
	name=[]
	for player in result:
		name.append(player.first_name + " " + player.last_name)
	context = {
		"title": "Every player who's last name is Cooper except Joshua",
		"results": name
	}
	return render(request, "leagues/results.html", context)


def alex_wyatt(request):
	result=Player.objects.filter(first_name="Alexander")|Player.objects.filter(first_name="Wyatt")
	name=[]
	for player in result:
		name.append(player.first_name + " " + player.last_name)
	context = {
		"title": "All player's with first name of Alexander OR Wyatt",
		"results": name
	}
	return render(request, "leagues/results.html", context)


####ORM2###################################################################

def team_atlantic(request):
	result=Team.objects.filter(league__name="Atlantic Soccer Conference")
	name=[]
	for team in result:
		name.append(team.team_name)
	context = {
		"title": "all teams in the Atlantic Soccer Conference",
		"results": name
	}
	return render(request, "leagues/results.html", context)

def current_penguins(request):
	result=Player.objects.filter(curr_team="28")
	name=[]
	for player in result:
		name.append(player.first_name + " " + player.last_name)
	context = {
		"title": "all (current) players on the Boston Penguins",
		"results": name
	}
	return render(request, "leagues/results.html", context)

def current_icbc(request):
	result=Player.objects.filter(curr_team__league=League.objects.get(id="2"))
	name=[]
	for player in result:
		name.append(player.first_name + " " + player.last_name)
	context = {
		"title": "all (current) players in the International Collegiate Baseball Conference",
		"results": name
	}
	return render(request, "leagues/results.html", context)

def current_lopez(request):
	result=Player.objects.filter(curr_team__league=League.objects.get(id="7")).filter(last_name="Lopez")
	name=[]
	for player in result:
		name.append(player.first_name + " " + player.last_name)
	context = {
		"title": "all (current) players in the American Conference of Amateur Football with last name 'Lopez'",
		"results": name
	}
	return render(request, "leagues/results.html", context)

def all_football(request):
	result=Player.objects.filter(all_teams__league=League.objects.get(id="7"))|Player.objects.filter(all_teams__league=League.objects.get(id="9"))
	name=[]
	for player in result:
		name.append(player.first_name + " " + player.last_name)
	context = {
		"title": "all football players",
		"results": name
	}
	return render(request, "leagues/results.html", context)

def team_current_sophia(request):
	result=Team.objects.filter(curr_players__first_name="Sophia")
	name=[]
	for team in result:
		name.append(team.team_name)
	context = {
		"title": "all teams with a (current) player named 'Sophia'",
		"results": name
	}
	return render(request, "leagues/results.html", context)

def league_current_sophia(request):
	result=League.objects.filter(teams__curr_players__first_name="Sophia")
	name=[]
	for league in result:
		name.append(league.name)
	context = {
		"title": "all leagues with a (current) player named 'Sophia'",
		"results": name
	}
	return render(request, "leagues/results.html", context)

def flores_norough(request):
	result=Player.objects.filter(last_name="Flores").exclude(curr_team__team_name="Washington Roughriders")
	name=[]
	for player in result:
		name.append(player.first_name + " " + player.last_name)
	context = {
		"title": ".everyone with the last name 'Flores' who DOESN'T (currently) play for the Washington Roughriders",
		"results": name
	}
	return render(request, "leagues/results.html", context)

def sam_evans(request):
	result=Team.objects.filter(all_players__first_name="Samuel",all_players__last_name="Evans")
	name=[]
	for team in result:
		name.append(team.team_name)
	context = {
		"title": "all teams, past and present, that Samuel Evans has played with",
		"results": name
	}
	return render(request, "leagues/results.html", context)

def tiger_cat(request):
	result=Player.objects.filter(all_teams__id="37")|Player.objects.filter(curr_team__id="37")
	name=[]
	for player in result:
		name.append(player.first_name + " " + player.last_name)
	context = {
		"title": "all players, past and present, with the Manitoba Tiger-Cats",
		"results": name
	}
	return render(request, "leagues/results.html", context)

def formerly_viking(request):
	result=Player.objects.filter(all_teams="40").exclude(curr_team="40")
	name=[]
	for player in result:
		name.append(player.first_name + " " + player.last_name)
	context = {
		"title": "all players who were formerly (but aren't currently) with the Wichita Vikings",
		"results": name
	}
	return render(request, "leagues/results.html", context)

def gray_before_colts(request):
	result=Team.objects.filter(all_players__first_name="Jacob")|Team.objects.filter(all_players__last_name="Gray")
	name=[]
	for team in result:
		if team.team_name == "Colts":
			break
		name.append(team.team_name)
	context = {
		"title": "every team that Jacob Gray played for before he joined the Oregon Colts",
		"results": name
	}
	return render(request, "leagues/results.html", context)

def josh_in_afabp(request):
	result=Player.objects.filter(first_name="Joshua").filter(all_teams__league__name="Atlantic Federation of Amateur Baseball Players")
	name=[]
	for player in result:
		name.append(player.first_name + " " + player.last_name)
	context = {
		"title": "everyone named 'Joshua' who has ever played in the Atlantic Federation of Amateur Baseball Players",
		"results": name
	}
	return render(request, "leagues/results.html", context)

###FIX > 12
def team_greaterthan_twelve(request):
	result=Team.objects.annotate(num_players=Count('all_players'))
	name=[]
	for team in result:
		if (num_players > 11):
			name.append(team.team_name)
	context = {
		"title": "all teams that have had 12 or more players, past and present.",
		"results": name
	}
	return render(request, "leagues/results.html", context)
###FIX > 12

def player_sorted(request):
	result=Player.objects.annotate(num_team=Count('all_teams__team_name')).order_by('-num_team')
	name=[]
	for player in result:
		name.append(player.first_name + " " + player.last_name)
	context = {
		"title": "all players, sorted by the number of teams they've played for",
		"results": name
	}
	return render(request, "leagues/results.html", context)





def go_back(request):
	return redirect("/chapters")




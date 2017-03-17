from django.shortcuts import render, redirect
from .models import League, Team, Player

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


def go_back(request):
	return redirect("/chapters")




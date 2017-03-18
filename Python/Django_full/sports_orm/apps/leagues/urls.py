from django.conf.urls import url
from . import views

urlpatterns = [
	url(r"^$", views.index, name="index"),
	url(r"^make_data/", views.make_data, name="make_data"),
  url(r'^chapters/', views.chapters, name='chapters'),


  url(r'^baseball_leagues', views.baseball_leagues, name='chapters'),
  url(r'^all_women_leagues', views.all_women_leagues, name='chapters'),
  url(r'^all_leagues_hockey', views.all_leagues_hockey, name='chapters'),
  url(r'^other_than_football', views.other_than_football, name='chapters'),
  url(r'^all_conferences', views.all_conferences, name='chapters'),
  url(r'^atlantic_leagues', views.atlantic_leagues, name='chapters'),
  url(r'^teams_dallas', views.teams_dallas, name='chapters'),
  url(r'^raptors', views.raptors, name='chapters'),
  url(r'^all_city', views.all_city, name='chapters'),
  url(r'^all_t', views.all_t, name='chapters'),
  url(r'^location_alpha', views.location_alpha, name='chapters'),
  url(r'^team_reverse', views.team_reverse, name='chapters'),
  url(r'^all_cooper', views.all_cooper, name='chapters'),
  url(r'^all_josh', views.all_josh, name='chapters'),
  url(r'^except_josh', views.except_josh, name='chapters'),
  url(r'^alex_wyatt', views.alex_wyatt, name='chapters'),

  #ORM2

  url(r'^team_atlantic', views.team_atlantic, name='chapters'),
  url(r'^current_penguins', views.current_penguins, name='chapters'),
  url(r'^current_icbc', views.current_icbc, name='chapters'),
  url(r'^current_lopez', views.current_lopez, name='chapters'),
  url(r'^all_football', views.all_football, name='chapters'),
  url(r'^team_current_sophia', views.team_current_sophia, name='chapters'),
  url(r'^league_current_sophia', views.league_current_sophia, name='chapters'),
  url(r'^flores_norough', views.flores_norough, name='chapters'),

  url(r'^sam_evans', views.sam_evans, name='chapters'),
  url(r'^tiger_cat', views.tiger_cat, name='chapters'),
  url(r'^formerly_viking', views.formerly_viking, name='chapters'),
  url(r'^gray_before_colts', views.gray_before_colts, name='chapters'),
  url(r'^josh_in_afabp', views.josh_in_afabp, name='chapters'),
  url(r'^team_greaterthan_twelve', views.team_greaterthan_twelve, name='chapters'),
  url(r'^player_sorted', views.player_sorted, name='chapters'),

  url(r'^go_back', views.go_back),

]
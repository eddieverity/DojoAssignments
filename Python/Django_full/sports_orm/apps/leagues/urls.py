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

  url(r'^go_back', views.go_back),

]
from django.conf.urls import url


from app import views, epic_battle_math

urlpatterns = [
  url('^$', views.index, name='index'),
  url('^test/', views.test, name='test'),
  url('^test2/', views.test2, name='test2'),
  url('^test4/', views.test4, name='test4'),
  url('^profile/', views.profile, name='profile'),
  url('^oxford/', views.oxford, name='oxford'),
  url('^calculator/', views.calculator, name='calculator'),
  url('^versions/', views.show_app_version, name='versions'),
  url('^google_analytics/', views.postman_google_analytics, name='postman_google_analytics'),
  url('^epic_battle/', epic_battle_math.fortress_battle, name='epic_battle'),
  url('^test5/', views.test5, name='test5'),




]



from django.urls import path
from . import views

urlpatterns = [
path('', views.home, name='home'),
path('user/<int:pk>', views.UserDetail.as_view(), name='user'),
path('kor', views.update_profile, name='kor'),
path('osati/unos', views.OsatiCreate.as_view(), name='osati-unos'),
path('osati', views.PregledOSati.as_view(), name='osati-pregled'),
path('osati1', views.KrajVremena.as_view(), name='krajvremena'),
path("register/", views.register, name="register"),
path('registered/', views.home, name='registered'),
path('osati/<int:pk>/update', views.OSatiUpdate.as_view(), name='osati-update'),
path('zadaci/unos', views.ListaZCreate.as_view(), name='zadaci-unos'),
path('zadaci', views.PregledZ.as_view(), name='zadaci-pregled'),
path('zadacir', views.PregledZR.as_view(), name='zadacir-pregled'),
path('zadaci/<int:pk>/update', views.ZadaciUpdate.as_view(), name='zadaci-update'),
path('zadaci/<int:pk>',views.ZDetail.as_view(), name='zadatak-detail'),
path('zadacib/<int:pk>',views.ZadatakDelete.as_view(), name='zadatak-del'),
]
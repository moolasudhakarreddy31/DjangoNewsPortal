from django.urls import path,include
from Ahaapp import views


urlpatterns = [
    path('home/',views.home),
    path('moviesinfo/',views.moviesinfo),
    path('sportsinfo/',views.sportsinfo),
    path('politicsinfo/',views.politicsinfo)





]

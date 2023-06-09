from django.urls import path
from . import views

urlpatterns = [
    path("", views.challenge_list, name="index"),
    path("<int:month>/", views.monthly_challenge_number),
    path("<str:month>/", views.monthly_challenge, name="month_challenge"),
]

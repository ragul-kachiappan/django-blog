from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
# Create your views here.

monthly_challenges = {
    "january": "Eat no meat for the entire month",
    "february": "Walk for atleast 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes every day!",
    "april": "Eat no meat for the entire month",
    "may": "Walk for atleast 20 minutes every day!",
    "june": "Learn Django for at least 20 minutes every day!",
    "july": "Eat no meat for the entire month",
    "august": "Walk for atleast 20 minutes every day!",
    "september": "Learn Django for at least 20 minutes every day!",
    "october": "Eat no meat for the entire month",
    "november": "Walk for atleast 20 minutes every day!",
    "december": "Learn Django for at least 20 minutes every day!",
}

def monthly_challenge_number(request, month):
    month_keys = list(monthly_challenges.keys())

    if month > len(month_keys):
        return HttpResponseNotFound("Invalid month!")
    forward_month = month_keys[month - 1]
    return HttpResponseRedirect("/challenges/" + forward_month)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
    except:
        return HttpResponseNotFound("This month is not supported!")
    return HttpResponse(challenge_text)
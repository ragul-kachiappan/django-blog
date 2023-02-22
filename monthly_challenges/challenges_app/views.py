from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# from django.template.loader import render_to_string
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
    redirect_path = reverse("month_challenge", args=[forward_month]) #figures out the path. pass the dynamic path inside args
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges_app/challenge.html")
    except:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")

def challenge_list(request):
    list_items = ""
    month_keys = list(monthly_challenges.keys())
    for month in month_keys:
        capitalized_month = month.capitalize()
        month_path = reverse("month_challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)
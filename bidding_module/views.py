from django.http import HttpResponse
from django.shortcuts import render




def home_page(request):
    context = {
        "title": "Bidding Module",
        "content" : "You can Bidding on an item"
    }

    return render(request, "home_page.html" , context)
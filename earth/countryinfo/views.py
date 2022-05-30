from django.shortcuts import render
import requests
# Create your views here.
def universe(request):
    url=f"https://restcountries.com/v2/all"
    res=requests.get(url)
    data = res.json()
    final= { 
        "info":data
    }
    return render(request, 'base.html', final )


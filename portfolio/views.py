from django.shortcuts import render

# Create your views here.


def portfolio(request):
    return render(request, 'portfolio/portfolio.html')


def home(request):
    return render(request, 'portfolio/home.html')

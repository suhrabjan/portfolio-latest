from django.urls import path
from . import views


urlpatterns = [
    path('portfolio/', views.portfolio, name='portfolio-portfolio'),
    path('', views.home, name='portfolio-home'),
]

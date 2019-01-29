from django.shortcuts import render
from mainpage.models import Main
from promopage.models import Promo
from teampage.models import Team
from clientpage.models import Client
from productpage.models import Product

def mainpage_list(request):
    mainpage = Main.objects.all()
    promopage = Promo.objects.all()
    teampage = Team.objects.all()
    clientpage = Client.objects.all()
    productpage = Product.objects.all()
    return render(request, "mainpage/mainpage_list.html", {"mainpage": mainpage,"promopage": promopage,"teampage": teampage,"clientpage": clientpage,"productpage": productpage})
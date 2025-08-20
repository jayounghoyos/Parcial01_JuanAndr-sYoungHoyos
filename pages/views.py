from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
# Create your views here.
    
class HomePageView(TemplateView):
    template_name = "pages/home.html"

class Cuelos:
    products = [
        {"id":"1", "name":"rionegro guatapé", "tipo": "comercial", "precio":"3232321"},
        {"id":"1", "name":"rionegro medellin", "tipo": "comercial", "precio":"3232321"},
        {"id":"1", "name":"rionegro caldas", "tipo": "comercial", "precio":"3232321"},
        {"id":"1", "name":"rionegro nariño", "tipo": "comercial", "precio":"3232321"},
    ]
class VuelosIndexView(View):
    template_name = 'Vuelos/index.html'
    
    def get(self, request):
        viewData = {}
        viewData["title"] = "vuelos"
        viewData["subtitle"] = "List of vuelos"
        viewData["Vueloss"] = Vuelos.products
        return render(request, self.template_name, viewData)
class VuelosShowView(View):
    template_name = 'vuelos/show.html'
    def get(self, request, id):
        viewData = {}
        product = Vuelos.products[int(id)-1]
        viewData["title"] = product["name"] + " - vuelos"
        viewData["subtitle"] = product["name"] + " vuelos information"
        viewData["product"] = product
        return render(request, self.template_name, viewData)
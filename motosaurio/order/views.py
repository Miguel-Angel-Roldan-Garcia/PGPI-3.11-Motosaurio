from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class OrderInformation(TemplateView):
    def getInformation(request):
        return render(request)
from django.shortcuts import render
from .models import Empresa
 
def empresa_detail(request):        
    empresa = Empresa.objects.first()
    return render(request, 'empresa/detail.html', {'empresa':empresa})
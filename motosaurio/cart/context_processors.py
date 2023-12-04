from .cesta import Cesta

def cart(request):
 return {'cart': Cesta(request)}

from decimal import Decimal
from django.conf import settings
from shop.models import Product
class Cesta:
    def __init__(self, request):
        self.session = request.session
        cesta = self.session.get(settings.CART_SESSION_ID)
        if not cesta:
            cesta = self.session[settings.CART_SESSION_ID] = {}
        self.cesta = cesta

    def add(self, product, quantity=1, override_quantity=False):
        product_id = str(product.id)
        if product_id not in self.cesta:
            self.cesta[product_id] = {'quantity': 0,
        'price': str(product.price)}
        if override_quantity:
            self.cesta[product_id]['quantity'] = quantity
        else:
            self.cesta[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cesta:
            del self.cesta[product_id]
            self.save()

    def __iter__(self):
        product_ids = self.cesta.keys()
        products = Product.objects.filter(id__in=product_ids)
        cesta = self.cesta.copy()
        for product in products:
            cesta[str(product.id)]['product'] = product
        for item in cesta.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cesta.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cesta.values())
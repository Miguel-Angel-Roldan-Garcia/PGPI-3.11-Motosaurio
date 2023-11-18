from django.db import models

class Product(models.Model):

    TYPE_CHOICES = (
	('RU', 'RUEDAS'),
	('MO', 'MOTOR'),
	('FR', 'FRENOS'),
	('FI', 'FILTROS'),
	('EM', 'EMBRAGUE'),
	('ES', 'ESCAPE'),
	('MA', 'MANILLAR'),
    ('OT', 'OTROS')
    )

    PRODUCER_CHOICES = (
        ('KW', 'KAWASAKI'), 
        ('HO', 'HONDA'), 
        ('YA', 'YAMAHA'), 
        ('DU', 'DUCATI'), 
        ('KY', 'KYMCO'),
        ('OT', 'OTROS') 
    )
    name = models.CharField(max_length=200, verbose_name='Título')
    slug = models.SlugField(max_length=200)
    product_type= models.CharField(max_length=255, verbose_name='Tipo de producto', choices=TYPE_CHOICES, default='OT')
    producer = models.CharField(max_length=255, verbose_name='fabricante', choices=PRODUCER_CHOICES, default='OT')
    image = models.ImageField(upload_to='products/%Y/%m/%d',
                            blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10,
                                decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
            models.Index(fields=['-created']),
        ]
    def __str__(self):
        return self.name

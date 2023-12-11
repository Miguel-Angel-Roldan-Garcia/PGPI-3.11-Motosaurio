from django.db import models
from django.urls import reverse
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

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

    type_choices_dict = {key: value for key, value in TYPE_CHOICES}

    PRODUCER_CHOICES = (
        ('KA', 'KAWASAKI'), 
        ('HO', 'HONDA'), 
        ('YA', 'YAMAHA'), 
        ('DU', 'DUCATI'), 
        ('KY', 'KYMCO'),
        ('OT', 'OTROS') 
    )

    producers_dict = {key: value for key, value in PRODUCER_CHOICES}

    name = models.CharField(max_length=200, verbose_name='Título')
    slug = models.SlugField(max_length=200)
    product_type= models.CharField(max_length=255, verbose_name='Tipo de producto', choices=TYPE_CHOICES, default='OT')
    producer = models.CharField(max_length=255, verbose_name='fabricante', choices=PRODUCER_CHOICES, default='OT')
    image = models.ImageField(upload_to='motosaurio/shop/static/images',
                            blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10,
                                decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[str(self.id)])
    
    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
            models.Index(fields=['-created']),
        ]
    def __str__(self):
        return self.name

class ProductReview(models.Model):
    RATING_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]

    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)])
    opinion = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.product.name} - Rating: {self.rating}"
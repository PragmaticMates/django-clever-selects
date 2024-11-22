from django.db import models
from django.utils.translation import gettext_lazy as _


class CarBrand(models.Model):
    title = models.CharField(_('title'), max_length=128, unique=True)
    created = models.DateTimeField(_('created'), auto_now_add=True)
    modified = models.DateTimeField(_('modified'), auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'example_car_brands'
        verbose_name = _('car brand')
        verbose_name_plural = _('car brands')
        ordering = ['title', ]


class BrandModel(models.Model):
    brand = models.ForeignKey(CarBrand, verbose_name=_('car brand'))
    title = models.CharField(_('title'), max_length=128)
    created = models.DateTimeField(_('created'), auto_now_add=True)
    modified = models.DateTimeField(_('modified'), auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'example_brand_models'
        verbose_name = _('brand model')
        verbose_name_plural = _('brand models')
        unique_together = (('brand', 'title'),)
        ordering = ['brand', 'title', ]


class Car(models.Model):
    ENGINES = [
        ('DIESEL', _('Diesel')),
        ('GASOLINE', _('Gasoline'))
    ]
    COLORS = [
        ('RED', _('red')),
        ('GREEN', _('green')),
        ('BLUE', _('blue')),
        ('WHITE', _('white')),
        ('BLACK', _('black')),
        ('YELLOW', _('yellow')),
        ('SILVER', _('silver')),
        ('PINK', _('pink'))
    ]

    model = models.ForeignKey(BrandModel, verbose_name=_('car brand model'))
    engine = models.CharField(choices=ENGINES, max_length=8)
    color = models.CharField(choices=COLORS, max_length=8, blank=True, null=True, default=None)
    numberplate = models.CharField(max_length=16, unique=True)
    created = models.DateTimeField(_('created'), auto_now_add=True)
    modified = models.DateTimeField(_('modified'), auto_now=True)

    def __str__(self):
        return '%(brand)s %(model)s' % {
            'brand': self.brand,
            'model': self.model,
        }

    @property
    def brand(self):
        return self.model.brand

    class Meta:
        db_table = 'example_cars'
        verbose_name = _('car')
        verbose_name_plural = _('cars')
        ordering = ['model__brand', 'model', 'numberplate']

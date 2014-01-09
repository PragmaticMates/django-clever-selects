from django.db import models
from django.utils.translation import ugettext_lazy as _


class CarBrand(models.Model):
    title = models.CharField(_(u'title'), max_length=128, unique=True)
    created = models.DateTimeField(_(u'created'), auto_now_add=True)
    modified = models.DateTimeField(_(u'modified'), auto_now=True)

    def __unicode__(self):
        return self.title

    class Meta:
        db_table = 'example_car_brands'
        verbose_name = _(u'car brand')
        verbose_name_plural = _(u'car brands')
        ordering = ['title', ]


class BrandModel(models.Model):
    brand = models.ForeignKey(CarBrand, verbose_name=_(u'car brand'))
    title = models.CharField(_(u'title'), max_length=128)
    created = models.DateTimeField(_(u'created'), auto_now_add=True)
    modified = models.DateTimeField(_(u'modified'), auto_now=True)

    def __unicode__(self):
        return self.title

    class Meta:
        db_table = 'example_brand_models'
        verbose_name = _(u'brand model')
        verbose_name_plural = _(u'brand models')
        unique_together = (('brand', 'title'),)
        ordering = ['brand', 'title', ]


class Car(models.Model):
    ENGINES = [
        ('DIESEL', _(u'Diesel')),
        ('GASOLINE', _(u'Gasoline'))
    ]
    COLORS = [
        ('RED', _(u'red')),
        ('GREEN', _(u'green')),
        ('BLUE', _(u'blue')),
        ('WHITE', _(u'white')),
        ('BLACK', _(u'black')),
        ('YELLOW', _(u'yellow')),
        ('SILVER', _(u'silver')),
        ('PINK', _(u'pink'))
    ]

    model = models.ForeignKey(BrandModel, verbose_name=_(u'car brand model'))
    engine = models.CharField(choices=ENGINES, max_length=8)
    color = models.CharField(choices=COLORS, max_length=8, blank=True, null=True, default=None)
    numberplate = models.CharField(max_length=16, unique=True)
    created = models.DateTimeField(_(u'created'), auto_now_add=True)
    modified = models.DateTimeField(_(u'modified'), auto_now=True)

    def __unicode__(self):
        return u'%(brand)s %(model)s' % {
            'brand': self.brand,
            'model': self.model,
        }

    @property
    def brand(self):
        return self.model.brand

    class Meta:
        db_table = 'example_cars'
        verbose_name = _(u'car')
        verbose_name_plural = _(u'cars')
        ordering = ['model__brand', 'model', 'numberplate']

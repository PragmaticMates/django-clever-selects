from django.core.urlresolvers import reverse_lazy
from django.forms import ChoiceField, ModelChoiceField
from django.utils.translation import gettext_lazy as _

from clever_selects.form_fields import ChainedChoiceField, ChainedModelChoiceField
from clever_selects.forms import ChainedChoicesForm, ChainedChoicesModelForm

from helpers import CONTINENTS, GENDER
from models import CarBrand, Car, BrandModel


class SimpleChainForm(ChainedChoicesForm):
    gender = ChoiceField(choices=[('', _('Select a gender'))] + list(GENDER))
    name = ChainedChoiceField(parent_field='gender', ajax_url=reverse_lazy('ajax_chained_names'), empty_label=_('Select name'))


class MultipleChainForm(ChainedChoicesForm):
    continent = ChoiceField(choices=[('', _('Select a continent'))] + list(CONTINENTS))
    country = ChainedChoiceField(parent_field='continent', ajax_url=reverse_lazy('ajax_chained_countries'))
    city = ChainedChoiceField(parent_field='country', ajax_url=reverse_lazy('ajax_chained_cities'))


class ModelChainForm(ChainedChoicesModelForm):
    brand = ModelChoiceField(queryset=CarBrand.objects.all(), required=True, empty_label=_('Select a car brand'))
    model = ChainedModelChoiceField(parent_field='brand', ajax_url=reverse_lazy('ajax_chained_models'),
                                    empty_label=_('Select a car model'), model=BrandModel, required=True)
    engine = ChoiceField(choices=([('', _('All engine types'))] + Car.ENGINES), required=False)
    color = ChainedChoiceField(parent_field='model', ajax_url=reverse_lazy('ajax_chained_colors'),
                               empty_label=_('Select a car model'), required=False)

    class Meta:
        model = Car
        fields = ['brand', 'model', 'engine', 'color', 'numberplate']

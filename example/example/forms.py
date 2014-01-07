from django.core.urlresolvers import reverse_lazy
from django.forms import ChoiceField
from django.utils.translation import ugettext_lazy as _

from clever_selects.form_fields import ChainedChoiceField
from clever_selects.forms import ChainedChoicesForm

from helpers import CONTINENTS, GENDER


class SimpleChainForm(ChainedChoicesForm):
    gender = ChoiceField(choices=[('', _(u'Select a gender'))] + list(GENDER))
    name = ChainedChoiceField(parent_field='gender', ajax_url=reverse_lazy('ajax_chained_names'))


class MultipleChainForm(ChainedChoicesForm):
    continent = ChoiceField(choices=[('', _(u'Select a continent'))] + list(CONTINENTS))
    country = ChainedChoiceField(parent_field='continent', ajax_url=reverse_lazy('ajax_chained_countries'))
    city = ChainedChoiceField(parent_field='country', ajax_url=reverse_lazy('ajax_chained_cities'))


#class ModelChainForm(ModelChainedChoicesForm):
    #car = forms.ModelChoiceField(queryset=Car.objects.all(), required=True, empty_label=_(u'Select a car brand'))
    #model = ChainedChoiceField(parent_field='car', ajax_url=reverse_lazy('ajax_chained_car_models'), empty_label=_(u'Select a car model'), required=True)
    #engine = forms.ChoiceField(choices=([('', _('All engine types'))] + Car.ENGINES), required=False)

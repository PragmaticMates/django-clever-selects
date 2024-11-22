from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.utils.encoding import smart_unicode
from django.utils.translation import gettext_lazy as _, gettext
from django.views.generic import FormView, TemplateView, CreateView, UpdateView, View
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import DeletionMixin

from clever_selects.views import ChainedSelectChoicesView

from forms import SimpleChainForm, MultipleChainForm, ModelChainForm
from helpers import NAMES, COUNTRIES, CITIES
from models import BrandModel, Car


class HomeView(TemplateView):
    template_name = 'home.html'


class ExampleFormViewMixin(object):
    def get_context_data(self, **kwargs):
        context_data = super(ExampleFormViewMixin, self).get_context_data(**kwargs)
        context_data['title'] = self.title
        try:
            context_data['message'] = self.request.session.get('message')
            del self.request.session['message']
        except KeyError:
            pass
        return context_data

    def get_success_url(self):
        return reverse(self.success_url)

    def form_valid(self, form):
        self.request.session['message'] = _('Form is valid! Submitted data: %s') % smart_unicode(
            form.cleaned_data, errors='replace')
        return super(ExampleFormViewMixin, self).form_valid(form)

    def form_invalid(self, form):
        self.message = _('Form is invalid!')
        return super(ExampleFormViewMixin, self).form_invalid(form)


class SimpleChainView(ExampleFormViewMixin, FormView):
    form_class = SimpleChainForm
    template_name = 'form.html'
    success_url = 'simple_chain'
    title = _('Simple chain')


class MultipleChainView(ExampleFormViewMixin, FormView):
    form_class = MultipleChainForm
    template_name = 'form.html'
    success_url = 'multiple_chain'
    title = _('Multiple chain')


class ModelChainView(ExampleFormViewMixin, CreateView):
    form_class = ModelChainForm
    template_name = 'cars.html'
    success_url = 'model_chain'
    title = _('Model chain')

    def get_context_data(self, **kwargs):
        context_data = super(ModelChainView, self).get_context_data(**kwargs)
        context_data['car_list'] = self.get_car_list()
        return context_data

    def get_car_list(self):
        return Car.objects.all()


class EditCarView(ExampleFormViewMixin, UpdateView):
    form_class = ModelChainForm
    template_name = 'form.html'
    success_url = 'model_chain'
    title = _('Update car')
    model = Car


class DeleteCarView(DeletionMixin, SingleObjectMixin, View):
    success_url = 'model_chain'
    model = Car

    def get(self, *args, **kwargs):
        return self.delete(*args, **kwargs)

    def get_success_url(self):
        return reverse(self.success_url)


class AjaxChainedNames(ChainedSelectChoicesView):
    def get_choices(self):
        choices = []
        try:
            gender_names = NAMES[self.parent_value]
            for name in gender_names:
                choices.append((name, name))
        except KeyError:
            return []
        return choices


class AjaxChainedCountries(ChainedSelectChoicesView):
    def get_choices(self):
        choices = []
        try:
            continent_countries = COUNTRIES[self.parent_value]
            for country in continent_countries:
                choices.append((country, country))
        except KeyError:
            return []
        return choices


class AjaxChainedCities(ChainedSelectChoicesView):
    def get_choices(self):
        choices = []
        try:
            country_cities = CITIES[self.parent_value]
            for city in country_cities:
                choices.append((city, city))
        except KeyError:
            return []
        return choices


class AjaxChainedModels(ChainedSelectChoicesView):
    def get_child_set(self):
        return BrandModel.objects.filter(brand__pk=self.parent_value)


class AjaxChainedColors(ChainedSelectChoicesView):
    def get_choices(self):
        choices = []
        try:
            model = BrandModel.objects.get(pk=self.parent_value)
            if 'Sportback' in model.title or 'Cabrio' in model.title or 'Coupe' in model.title:
                return [
                    ('RED', gettext('red')),
                    ('WHITE', gettext('white')),
                    ('BLACK', gettext('black')),
                    ('YELLOW', gettext('yellow')),
                    ('SILVER', gettext('silver')),
                ]
            for color in Car.COLORS:
                choices.append((color[0], gettext(color[1])))
            return choices
        except (ObjectDoesNotExist, KeyError):
            return []

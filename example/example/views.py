from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.views.generic import FormView, TemplateView

from clever_selects.views import ChainedSelectChoicesView

from forms import SimpleChainForm, MultipleChainForm
from helpers import COUNTRIES, CITIES, GENDER_MALE, GENDER_FEMALE


class HomeView(TemplateView):
    template_name = 'home.html'


class SimpleChainView(FormView):
    form_class = SimpleChainForm
    template_name = 'form.html'
    success_url = 'simple_chain'
    message = None

    def get_context_data(self, **kwargs):
        context_data = super(SimpleChainView, self).get_context_data(**kwargs)
        context_data['title'] = _(u'Simple chain')
        if 'message' in self.request.session:
            context_data['message'] = self.request.session['message']
            del self.request.session['message']
        return context_data

    def get_success_url(self):
        return reverse(self.success_url)

    def form_valid(self, form):
        self.request.session['message'] = _(u'Form is valid! Submitted data: %s') % form.cleaned_data
        return super(SimpleChainView, self).form_valid(form)

    def form_invalid(self, form):
        self.request.session['message'] = _(u'Form is invalid!')
        return super(SimpleChainView, self).form_invalid(form)


class MultipleChainView(FormView):
    form_class = MultipleChainForm
    template_name = 'form.html'
    success_url = 'multiple_chain'
    message = None

    def get_context_data(self, **kwargs):
        context_data = super(MultipleChainView, self).get_context_data(**kwargs)
        context_data['title'] = _(u'Multiple chain')
        if 'message' in self.request.session:
            context_data['message'] = self.request.session['message']
            del self.request.session['message']
        return context_data

    def get_success_url(self):
        return reverse(self.success_url)

    def form_valid(self, form):
        self.request.session['message'] = _(u'Form is valid! Submitted data: %s') % form.cleaned_data
        return super(MultipleChainView, self).form_valid(form)

    def form_invalid(self, form):
        self.request.session['message'] = _(u'Form is invalid!')
        return super(MultipleChainView, self).form_invalid(form)


class AjaxChainedNames(ChainedSelectChoicesView):
    NAMES = {
        GENDER_MALE: ['Andrew', 'Arthur', 'Ian', 'Eric', 'Leonard', 'Lukas', 'Matt', 'Peter', 'Vincent'],
        GENDER_FEMALE: ['Allison', 'Angela', 'Catherine', 'Elisabeth', 'Evangeline', 'Heidi', 'Katie', 'Lilly', 'Susan']
    }

    def get_choices(self):
        choices = []
        try:
            gender_names = self.NAMES[self.parent_value]
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

'''
@author: Erik Telepovsky
'''

import json

from django.core.exceptions import ObjectDoesNotExist
from django.core.validators import EMPTY_VALUES
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse
from django.utils.cache import add_never_cache_headers
from django.views.generic.base import View


class ChainedSelectFormViewMixin(object):

    def get_form_kwargs(self):
        kwargs = super(ChainedSelectFormViewMixin, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class ChainedSelectChoicesView(View):
    child_set = None

    def dispatch(self, request, *args, **kwargs):
        self.field = request.GET.get("field")
        self.field_value = request.GET.get("field_value", None)
        self.parent_field = request.GET.get("parent_field")
        self.parent_value = request.GET.get("parent_value")
        if self.parent_value in EMPTY_VALUES + ('None', ):
            return self.empty_response()
        return super(ChainedSelectChoicesView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        response = HttpResponse(
            json.dumps(self.get_choices(), cls=DjangoJSONEncoder),
            content_type='application/javascript'
        )
        add_never_cache_headers(response)
        return response

    def empty_response(self):
        response = HttpResponse(
            json.dumps((), cls=DjangoJSONEncoder),
            content_type='application/javascript'
        )
        add_never_cache_headers(response)
        return response

    def get_child_set(self):
        return self.child_set

    def get_choices(self):
        choices = []
        if self.parent_value in EMPTY_VALUES + ('None', ) or self.get_child_set() is None:
            return []
        try:
            for obj in self.get_child_set().all():
                choices.append((obj.pk, str(obj)))
            return choices
        except ObjectDoesNotExist:
            return []

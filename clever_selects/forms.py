__author__ = 'Erik Telepovsky'

import json

from django import forms
from django.core.exceptions import ObjectDoesNotExist
from django.core.validators import EMPTY_VALUES
from django.db import models

from form_fields import ChainedChoiceField, ChainedModelChoiceField
from testclient import TestClient


class ChainedChoicesMixin(object):
    """
    Form Mixin to be used with ChainedChoicesForm and ChainedChoicesModelForm.
    It loads the options when there is already an instance or initial data.
    """
    user = None
    prefix = None
    fields = []
    chained_fields_names = []
    chained_model_fields_names = []

    def init_chained_choices(self, *args, **kwargs):
        self.chained_fields_names = self.get_fields_names_by_type(ChainedChoiceField)
        self.chained_model_fields_names = self.get_fields_names_by_type(ChainedModelChoiceField)
        self.user = kwargs.get('user', self.user)

        if kwargs.get('data', None) is not None:
            self.set_choices_via_ajax(kwargs['data'])

        elif len(args) > 0 and args[0] not in EMPTY_VALUES:
            self.set_choices_via_ajax(args[0])

        elif kwargs.get('instance', None) is not None:
            oldest_parent_field_names = list(set(self.get_oldest_parent_field_names()))
            youngest_child_names = list(set(self.get_youngest_children_field_names()))

            for youngest_child_name in youngest_child_names:
                self.find_instance_attr(kwargs['instance'], youngest_child_name)

            for oldest_parent_field_name in oldest_parent_field_names:
                try:
                    self.fields[oldest_parent_field_name].initial = getattr(self, '%s' % oldest_parent_field_name)
                except AttributeError:
                    pass

            self.set_choices_via_ajax()

        elif 'initial' in kwargs and kwargs['initial'] not in EMPTY_VALUES:
            self.set_choices_via_ajax(kwargs['initial'], is_initial=True)
        else:
            for field_name in self.chained_fields_names + self.chained_model_fields_names:
                empty_label = self.fields[field_name].empty_label
                self.fields[field_name].choices = [('', empty_label)]

    def set_choices_via_ajax(self, kwargs=None, is_initial=False):
        for field_name in self.chained_fields_names + self.chained_model_fields_names:
            field = self.fields[field_name]
            try:
                c = TestClient()

                try:
                    if self.user:
                        c.login_user(self.user)
                except AttributeError:
                    pass

                if kwargs is not None:
                    # inital data do not have any prefix
                    if self.prefix in EMPTY_VALUES or is_initial:
                        parent_value = kwargs.get(field.parent_field, None)
                        field_value = kwargs.get(field_name, None)
                    else:
                        parent_value = kwargs.get('%s-%s' % (self.prefix, field.parent_field), None)
                        field_value = kwargs.get('%s-%s' % (self.prefix, field_name), None)
                else:
                    parent_value = getattr(self, '%s' % field.parent_field, None)
                    field_value = getattr(self, '%s' % field_name, None)

                field.choices = [('', field.empty_label)]

                # check that parent_value is valid
                if parent_value:
                    parent_value = getattr(parent_value, 'pk', parent_value)

                    url = field.ajax_url
                    params = {
                        'field_name': field_name,
                        'parent_value': parent_value,
                        'field_value': field_value
                    }
                    data = c.get(url, params)

                    try:
                        field.choices = field.choices + json.loads(data.content)
                    except ValueError:
                        raise ValueError(u'Data returned from ajax request (url=%(url)s, params=%(params)s) could not be deserialized to Python object' % {
                            'url': url,
                            'params': params
                        })

                field.initial = field_value

            except ObjectDoesNotExist:
                field.choices = ()

    def get_fields_names_by_type(self, type):
        result = []
        for field_name in self.fields:
            field = self.fields[field_name]
            if isinstance(field, type):
                result.append(field_name)
        return result

    def get_parent_fields_names(self):
        result = []
        for field_name in self.fields:
            field = self.fields[field_name]
            if hasattr(field, 'parent_field'):
                result.append(field.parent_field)
        return result

    def get_children_field_names(self, parent_name):
        if parent_name in EMPTY_VALUES:
            return []
        result = []
        for field_name in self.fields:
            field = self.fields[field_name]
            if getattr(field, 'parent_field', None) == parent_name:
                result.append(field_name)
        return result

    def get_chained_fields_names(self):
        chained_fields_names = self.get_fields_names_by_type(ChainedChoiceField)
        chained_model_fields_names = self.get_fields_names_by_type(ChainedModelChoiceField)
        return chained_fields_names + chained_model_fields_names

    def get_oldest_parent_field_names(self):
        chained_fields_names = self.get_fields_names_by_type(ChainedChoiceField)
        chained_model_fields_names = self.get_fields_names_by_type(ChainedModelChoiceField)

        oldest_parent_field_names = []
        for field_name in self.get_parent_fields_names():
            if field_name not in chained_fields_names and field_name not in chained_model_fields_names:
                oldest_parent_field_names.append(field_name)
        return oldest_parent_field_names

    def get_youngest_children_field_names(self):
        result = []
        chained_fields_names = self.get_fields_names_by_type(ChainedChoiceField)
        chained_model_fields_names = self.get_fields_names_by_type(ChainedModelChoiceField)

        for field_name in chained_fields_names + chained_model_fields_names:
            if field_name not in self.get_parent_fields_names():
                result.append(field_name)
        return result

    def find_instance_attr(self, instance, attr_name):
        field = self.fields[attr_name]
        if hasattr(instance, attr_name):
            attribute = getattr(instance, attr_name)
            attr_value = getattr(attribute, 'pk', unicode(attribute)) if attribute else None
            setattr(self, '%s' % attr_name, attr_value)

            if hasattr(field, 'parent_field'):
                parent_instance = attribute if isinstance(attribute, models.Model) else instance
                self.find_instance_attr(parent_instance, field.parent_field)


class ChainedChoicesForm(forms.Form, ChainedChoicesMixin):
    """
    Form class to be used with ChainedChoiceField and ChainedSelect widget
    If there is request POST data in *args (i.e. form validation was invalid)
    then the options will be loaded when the form is built.
    """
    def __init__(self, language_code=None, *args, **kwargs):
        super(ChainedChoicesForm, self).__init__(*args, **kwargs)
        self.language_code = language_code
        self.init_chained_choices(*args, **kwargs)

    def is_valid(self):
        if self.language_code:
            # response is not translated to requested language code :/
            # so translation is triggered manually
            from django.utils.translation import activate
            activate(self.language_code)
        return super(ChainedChoicesForm, self).is_valid()


class ChainedChoicesModelForm(forms.ModelForm, ChainedChoicesMixin):
    """
    Form class to be used with ChainedChoiceField and ChainedSelect widget
    If there is already an instance (i.e. editing)
    then the options will be loaded when the form is built.
    """
    def __init__(self, language_code=None, *args, **kwargs):
        super(ChainedChoicesModelForm, self).__init__(*args, **kwargs)
        self.language_code = language_code
        self.init_chained_choices(*args, **kwargs)

    def is_valid(self):
        if self.language_code:
            # response is not translated to requested language code :/
            # so translation is triggered manually
            from django.utils.translation import activate
            activate(self.language_code)
        return super(ChainedChoicesModelForm, self).is_valid()

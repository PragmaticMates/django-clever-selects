from __future__ import absolute_import

from django.core import validators
from django.core.exceptions import ValidationError
from django.forms import ChoiceField
from django.forms.models import ModelChoiceField, ModelMultipleChoiceField

from .widgets import ChainedSelect, ChainedSelectMultiple


class ChainedChoiceField(ChoiceField):
    def __init__(self, parent_field, ajax_url, choices=None, empty_label='--------', *args, **kwargs):
        self.parent_field = parent_field
        self.ajax_url = ajax_url
        self.choices = choices or (('', empty_label), )
        self.empty_label = empty_label

        defaults = {
            'widget': ChainedSelect(parent_field=parent_field, ajax_url=ajax_url, attrs={'empty_label': empty_label}),
        }
        defaults.update(kwargs)

        super(ChainedChoiceField, self).__init__(choices=self.choices, *args, **defaults)

    def valid_value(self, value):
        """Dynamic choices so just return True for now"""
        return True


class ChainedModelChoiceField(ModelChoiceField):
    def __init__(self, parent_field, ajax_url, model, empty_label='--------', *args, **kwargs):
        self.parent_field = parent_field
        self.ajax_url = ajax_url
        self.model = model
        # self.queryset = model.objects.all()  # Large querysets could take long time to load all values (django-cities)
        self.queryset = model.objects.none()
        self.empty_label = empty_label

        defaults = {
            'widget': ChainedSelect(parent_field=parent_field, ajax_url=ajax_url, attrs={'empty_label': empty_label}),
        }
        defaults.update(kwargs)

        super(ChainedModelChoiceField, self).__init__(queryset=self.queryset, empty_label=empty_label, *args, **defaults)

    def valid_value(self, value):
        """Dynamic choices so just return True for now"""
        return True

    def to_python(self, value):
        empty_values = getattr(self, 'empty_values', list(validators.EMPTY_VALUES))
        if value in empty_values:
            return None
        try:
            key = self.to_field_name or 'pk'
            value = self.model.objects.get(**{key: value})
        except (ValueError, self.queryset.model.DoesNotExist):
            raise ValidationError(self.error_messages['invalid_choice'], code='invalid_choice')
        return value

    def validate(self, value):
        """
        Validates that the input is in self.choices.
        """
        super(ChoiceField, self).validate(value)
        if value and not self.valid_value(value):
            raise ValidationError(
                self.error_messages['invalid_choice'],
                code='invalid_choice',
                params={'value': value},
            )


class ChainedModelMultipleChoiceField(ModelMultipleChoiceField):
    def __init__(self, parent_field, ajax_url, model, *args, **kwargs):
        self.parent_field = parent_field
        self.ajax_url = ajax_url
        self.model = model
        self.queryset = model.objects.all()

        defaults = {
            'widget': ChainedSelectMultiple(parent_field=parent_field, ajax_url=ajax_url),
        }
        defaults.update(kwargs)

        super(ChainedModelMultipleChoiceField, self).__init__(queryset=self.queryset, *args, **defaults)

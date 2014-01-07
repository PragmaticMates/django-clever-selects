from django.forms import ChoiceField
from django.forms.models import ModelChoiceField

from widgets import ChainedSelect


class ChainedChoiceField(ChoiceField):
    def __init__(self, parent_field, ajax_url, choices=None, empty_label='--------', *args, **kwargs):

        self.parent_field = parent_field
        self.ajax_url = ajax_url
        self.choices = choices or (('', empty_label), )

        defaults = {
            'widget': ChainedSelect(parent_field=parent_field, ajax_url=ajax_url, attrs={'empty_label': empty_label}),
        }
        defaults.update(kwargs)

        super(ChainedChoiceField, self).__init__(choices=self.choices, *args, **defaults)

    def valid_value(self, value):
        """Dynamic choices so just return True for now"""
        return True


class ChainedModelChoiceField(ModelChoiceField):
    def __init__(self, parent_field, ajax_url, model, *args, **kwargs):

        self.parent_field = parent_field
        self.ajax_url = ajax_url
        self.queryset = model.objects.all()

        defaults = {
            'widget': ChainedSelect(parent_field=parent_field, ajax_url=ajax_url),
        }
        defaults.update(kwargs)

        super(ChainedModelChoiceField, self).__init__(queryset=self.queryset, *args, **defaults)

    def valid_value(self, value):
        """Dynamic choices so just return True for now"""
        return True

from django.forms.widgets import Select, SelectMultiple


class ChainedSelectMixin(object):
    """
    A ChoiceField widget mixin where the options for the select are dependent on the value of the parent select field.
    When the parent field is changed, an ajax call is made to determine the options.

    Form must inherit from ChainedChoicesMixin (or from helper forms ChainedChoicesForm and ChainedChoicesModelForm)
    which loads the options when there is already an instance or initial data.
    """

    template_name = 'clever_selects/widgets/chained_select.html'

    def __init__(self, parent_field=None, ajax_url=None, *args, **kwargs):
        self.parent_field = parent_field
        self.ajax_url = ajax_url
        super(ChainedSelectMixin, self).__init__(*args, **kwargs)

    def get_context(self, name, value, attrs):
        context = super(ChainedSelectMixin, self).get_context(name, value, attrs)

        field_prefix = attrs['id'][:attrs['id'].rfind('-') + 1]

        if not field_prefix:
            parent_field_id = "id_" + self.parent_field
        else:
            parent_field_id = field_prefix + self.parent_field

        context['widget']['attrs']['ajax_url'] = self.ajax_url
        context['js_parent_field_id'] = parent_field_id
        context['js_chained_id'] = attrs['id']
        return context


class ChainedSelect(ChainedSelectMixin, Select):
    pass


class ChainedSelectMultiple(ChainedSelectMixin, SelectMultiple):
    pass

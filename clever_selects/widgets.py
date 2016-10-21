from django.forms.widgets import Select
from django.utils.safestring import mark_safe


class ChainedSelect(Select):
    """
    A ChoiceField widget where the options for the select are dependant on the value of the parent select field.
    When the parent field is changed an ajax call is made to determine the options.

    Form must inherit from ChainedChoicesMixin (or from helper forms ChainedChoicesForm and ChainedChoicesModelForm)
    which loads the options when there is already an instance or initial data.
    """
    def __init__(self, parent_field=None, ajax_url=None, *args, **kwargs):
        self.parent_field = parent_field
        self.ajax_url = ajax_url
        super(ChainedSelect, self).__init__(*args, **kwargs)

    class Media:
        js = ['js/clever-selects.js']

    def render(self, name, value, attrs={}, choices=()):
        field_prefix = attrs['id'][:attrs['id'].rfind('-') + 1]
        formset_prefix = attrs['id'][:attrs['id'].find('-') + 1]

        if not field_prefix:
            parentfield_id = "id_" + self.parent_field
        else:
            parentfield_id = field_prefix + self.parent_field

        attrs.update(self.attrs)
        attrs['ajax_url'] = self.ajax_url

        try:
            output = super(ChainedSelect, self).render(name, value, attrs=attrs, choices=choices)
        except TypeError:
            output = super(ChainedSelect, self).render(name, value, attrs=attrs)

        js = """
        <script type="text/javascript">
        //<![CDATA[
            $(document).ready(function(){
                var parent_field = $("#%(parentfield_id)s");
                parent_field.addClass('chained-parent-field');
                var chained_ids = parent_field.attr('chained_ids');
                if(chained_ids == null)
                    parent_field.attr('chained_ids', "%(chained_id)s");
                else
                    parent_field.attr('chained_ids', chained_ids + ",%(chained_id)s");
            });
        //]]>
        </script>

        """ % {"parentfield_id": parentfield_id, 'chained_id': attrs['id']}

#        TODO: check admin compatibility with this syntax:
#        js = """
#        <script type="text/javascript">
#        //<![CDATA[
#        (function($) {
#           ...
#        })(django.jQuery);
#        //]]>
#        </script>

        output += js

        return mark_safe(output)

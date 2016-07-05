from django.forms.widgets import Select, SelectMultiple
from django.utils.safestring import mark_safe
from django.utils.html import format_html
from django.forms.utils import flatatt


class ChainedSelectMixin(object):

    def __init__(self, parent_field=None, ajax_url=None, *args, **kwargs):
        self.parent_field = parent_field
        self.ajax_url = ajax_url
        super().__init__(*args, **kwargs)

    class Media:
        js = ['js/clever-selects.js']

    def render(self, name, value, attrs={}, choices=()):
        field_prefix = attrs['id'][:attrs['id'].rfind('-') + 1]

        if not field_prefix:
            parentfield_id = "id_" + self.parent_field
        else:
            parentfield_id = field_prefix + self.parent_field

        attrs.update(self.attrs)
        attrs['ajax_url'] = self.ajax_url

        js = """
        <script type="text/javascript">
            (function($) {
                $(document).ready(function(){
                    var parent_field = $("#%(parentfield_id)s");
                    parent_field.addClass('chained-parent-field');
                    var chained_ids = parent_field.attr('chained_ids');
                    if(chained_ids == null)
                        parent_field.attr('chained_ids', "%(chained_id)s");
                    else
                        parent_field.attr('chained_ids', chained_ids + ",%(chained_id)s");

                    parent_field.on('change', function() {
                        $(this).loadAllChainedChoices();
                    });
                });
            })(jQuery || django.jQuery);
        </script>
        """ % {"parentfield_id": parentfield_id, 'chained_id': attrs['id']}

        if value is None:
            value = ''
        final_attrs = self.build_attrs(attrs, name=name)
        output = [format_html(self.html_template, flatatt(final_attrs))]
        options = self.render_options(choices, [value])
        if options:
            output.append(options)
        output.append(js)
        output.append('</select>')
        return mark_safe('\n'.join(output))


#        TODO: check admin compatiblity with this syntax:
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


class ChainedSelect(ChainedSelectMixin, Select):
    """
    A ChoiceField widget where the options for the select are dependant on the value of the parent select field.
    When the parent field is changed an ajax call is made to determine the options.

    Form must inherit from ChainedChoicesMixin (or from helper forms ChainedChoicesForm and ChainedChoicesModelForm)
    which loads the options when there is already an instance or initial data.
    """
    html_template = '<select{}>'


class ChainedSelectMultiple(ChainedSelectMixin, SelectMultiple):
    html_template = '<select multiple="multiple"{}>'

    def render_options(self, choices, selected_choices):
        if selected_choices:
            return super().render_options(choices, selected_choices[0])
        return ''

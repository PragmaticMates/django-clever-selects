django-clever-selects
=====================

This library is inspired by **django-chained-selectbox** from *s-block*
(https://github.com/s-block/django-chained-selectbox).

It serves chained select box widget for Django framework using AJAX requests for chaining select boxes together.
The values change depending on the parent value.

Previous mentioned library was intended for use in Django admin only. The new library has frontend functionality,
improved existing instance data initialization and new ``ChainedModelChoiceField``. It also uses custom TestClient which
is able pass ``request.user`` variable into AJAX view if user is logged in. It is very useful if you need to filter result queryset by
user permissions for example.

Tested on Django 1.4.5.


Requirements
------------
- Django

- jQuery


Installation
------------

1. Install python library using pip: pip install django-clever-selects

2. Add ``clever_selects`` to ``INSTALLED_APPS`` in your Django settings file

3. Add ``clever_selects_extras`` to your ``{% load %}`` statement and put ``{% clever_selects_js_import %}`` tag before closing ``</body>`` element. It is important to load clever-selects.js file after body content, so do not put it in the <head></head>!


Usage
-----

Forms
'''''

Form must inherit from ``ChainedChoicesMixin`` (or from ``ChainedChoicesForm`` / ``ChainedChoicesModelForm``, depends on your needs)
which loads the options when there is already an instance or initial data::

    from clever_selects.form_fields import ChainedChoiceField
    from clever_selects.forms import ChainedChoicesForm


    class SimpleChainForm(ChainedChoicesForm):
        first_field = ChoiceField(choices=(('', '------------'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), ))
        second_field = ChainedChoiceField(parent_field='first_field', ajax_url=reverse_lazy('ajax_chained_view'))


    class MultipleChainForm(ChainedChoicesForm):
        first_field = ChoiceField(choices=(('', '------------'), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), ))
        second_field = ChainedChoiceField(parent_field='first_field', ajax_url=reverse_lazy('ajax_chained_view'))
        third_field = ChainedChoiceField(parent_field='second_field', ajax_url=reverse_lazy('ajax_chained_view'))
        fourth_field = ChainedChoiceField(parent_field='third_field', ajax_url=reverse_lazy('ajax_chained_view'))
        fifth_field = ChainedChoiceField(parent_field='fourth_field', ajax_url=reverse_lazy('ajax_chained_view'))


    class ModelChainForm(ChainedChoicesModelForm):
        brand = forms.ModelChoiceField(queryset=CarBrand.objects.all(), required=True,
            empty_label=_(u'Select a car brand'))
        model = ChainedModelChoiceField(parent_field='brand', ajax_url=reverse_lazy('ajax_chained_models'),
            empty_label=_(u'Select a car model'), model=BrandModel, required=True)
        engine = forms.ChoiceField(choices=([('', _('All engine types'))] + Car.ENGINES), required=False)
        color = ChainedChoiceField(parent_field='model', ajax_url=reverse_lazy('ajax_chained_colors'),
            empty_label=_(u'Select a car model'), required=False)

        class Meta:
            model = Car


Notice that ajax URLs could differ of each field for different purposes. See example project for more use cases.

In order to pre-populate child fields, the form can need to have access to the current user. This can be done by passing
the user to the kwargs of the form's __init__() method in the form's view. The ChainedSelectFormViewMixin takes care
of this for you.::

    class CreateCarView(ChainedSelectFormViewMixin, CreateView)
        template_name = "create_car.html"
        form_class = ModelChainForm
        model = Car

Views
'''''

Ajax call is made whenever the parent field is changed. You must set up the ajax URL to return json list of lists::

    class AjaxChainedView(BaseDetailView):
        """
        View to handle the ajax request for the field options.
        """

        def get(self, request, *args, **kwargs):
            field = request.GET.get('field')
            parent_value = request.GET.get("parent_value")

            vals_list = []
            for x in range(1, 6):
                vals_list.append(x*int(parent_value))

            choices = tuple(zip(vals_list, vals_list))

            response = HttpResponse(
                json.dumps(choices, cls=DjangoJSONEncoder),
                mimetype='application/javascript'
            )
            add_never_cache_headers(response)
            return response


Or you can use ``ChainedSelectChoicesView`` class helper like this::

    class AjaxChainedView(ChainedSelectChoicesView):
        def get_choices(self):
            vals_list = []
            for x in range(1, 6):
                vals_list.append(x*int(self.parent_value))
            return tuple(zip(vals_list, vals_list))

or like this::

    class AjaxChainedView(ChainedSelectChoicesView):
        def get_child_set(self):
            return ChildModel.object.filter(parent_id=self.parent_value)

Don't forget to update your urls.py::

    url(r'^ajax/custom-chained-view-url/$', AjaxChainedView.as_view(), name='ajax_chained_view'),

Authors
-------

Library is by `Erik Telepovsky` from `Pragmatic Mates`_. See `our other libraries`_.

.. _Pragmatic Mates: http://www.pragmaticmates.com/
.. _our other libraries: https://github.com/PragmaticMates
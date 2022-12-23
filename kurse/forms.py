from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Div, Field, HTML
from django import forms


class ClassCreateForm(forms.Form):
    name = forms.CharField(
        label="Netz",
        required=True,
    )
    is_active = forms.BooleanField(
        label="aktiv",
        required=False,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            Div(
                Field(
                    'name',
                    css_class='form-control form-control-sm',
                ),
                Field(
                    'is_active',
                    css_class='form-control form-control-sm',
                )
            )
        )
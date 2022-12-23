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
        self.sign_data = kwargs.pop('sign_data', None)
        self.sign = self.sign_data.get('sign')
        self.aktion = kwargs.pop('aktion', None)
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            Div(
                Div(

                    Div(
                        Field(
                            'name',
                            css_class='form-control form-control-sm',
                        ),
                        css_class='col-12 col-sm-6 col-md-4'
                    ),
                    Div(
                        Field(
                            'is_active',
                            css_class='form-check-input',
                        ),
                        css_class='col-12 col-sm-2'
                    ),
                    HTML(""),
                    Div(
                        FormActions(
                            Submit(
                                'submit',
                                'speichern',
                                css_class='btn-primary btn-sm align-bottom send-button col-12 col-sm-5 pp-mtb-2',
                                css_id='speichern'
                            ),
                            Submit(
                                'delete',
                                'löschen',
                                css_class='btn-danger btn-sm align-bottom send-button col-12 col-sm-5 pp-mtb-2',
                                css_id='delete'
                            ),
                            css_class='col-12 pp-mb-5'
                        ),
                        css_class='col-12 col-sm-6 col-md-4 btn-group left'
                    ),
                    css_class="row d-flex align-items-end"
                ),
            )
        )
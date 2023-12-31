from datetime import datetime

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field
from django import forms
from django.utils.translation import gettext as _

from .models import Employee


class CreateEmployeeForm(forms.ModelForm):
    supervisor = forms.ModelChoiceField(
        label=_("Supervisor"),
        help_text=_("Assign a manager to the employee"),
        queryset=Employee.objects.exclude(job_title="JR"))

    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.layout = Layout(
        Field('first_name'),
        Field('last_name'),
        Field('date_offered'),
        Field('job_title'),
        Field('salary'),
        Field('supervisor'),
    )

    class Meta:
        model = Employee
        fields = [
            "first_name",
            "last_name",
            "salary",
            "date_offered",
            "supervisor",
            "photo",
        ]
        labels = {
            "first_name": _("Name"),
            "last_name": _("Last name"),
            "job_title": _("Position"),
            "date_offered": _("Date offered"),
            "salary": _("Salary")
        }
        help_texts = {
            "first_name": _("Enter the employee's name"),
            "last_name": _("Enter the employee's last name"),
            "job_title": _("Specify the employee's position"),
            "date_offered": _("Indicate the date the employee was hired"),
            "salary": _("Set employee salary")
        }
        widgets = {
            "date_offered": forms.SelectDateWidget(
                years=range(datetime.now().year, 1970, -1),
            ),
        }

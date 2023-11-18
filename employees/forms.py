from django import forms
from django.utils.translation import gettext as _

from .models import Employee


class CreateEmployeeForm(forms.ModelForm):

    supervisor = forms.ModelChoiceField(label=_("Supervisor"),
                                        help_text=_("Assign a manager to the employee"),
                                        queryset=Employee.objects.exclude(job_title="JR"))

    class Meta:
        model = Employee
        exclude = [
            "date_created",
        ]
        labels = {
            "first_name": _("Name"),
            "last_name": _("Last name"),
            "job_title": _("Position"),
            "date_offered": _("Offer date"),
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
            "date_offered": forms.DateInput(attrs={"type": "date"}),
        }
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class RateProfessorForm(forms.Form):
    difficulty = forms.ChoiceField(
        label="Difficulty",
        choices=(
            ("A", "A"),
            ("B", "B"),
            ("C", "C"),
            ("D", "D"),
            ("F", "F"),
        ),
        required=True,
    )
    grade = forms.ChoiceField(
        label="Grade",
        choices=(
            ("A", "A"),
            ("B", "B"),
            ("C", "C"),
            ("D", "D"),
            ("F", "F"),
        ),
        required=True,
    )
    pro_student = forms.BooleanField(label="Pro Student", required=False)
    organized = forms.BooleanField(label="Organized", required=False)

    def __init__(self, *args, **kwargs):
        super(RateProfessorForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.form_action = "rate_professor"
        self.helper.add_input(Submit("submit", "Rate Professor"))

class CreateProfessorForm(forms.Form):
    first_name = forms.CharField(
        label="First Name", max_length=100, widget=forms.TextInput, required=True
    )
    last_name = forms.CharField(
        label="Last Name", max_length=100, widget=forms.TextInput, required=True
    )
    college = forms.ChoiceField(
        label="College",
        choices=(
            ("UPRRP", "UPRRP"),
            ("UPRM", "UPRM"),
            ("UPRA", "UPRA"),
    ), required=True,
    )

    faculty = forms.ChoiceField(
        label="Faculty",
        choices=(
            ("Humanidades", "Humanidades"),
            ("Ciencias Naturales", "Ciencias Naturales"),
        ), required=True,
    )



    def __init__(self, *args, **kwargs):
        super(CreateProfessorForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.form_action = "create_professor"
        self.helper.add_input(Submit("submit", "Create Professor"))
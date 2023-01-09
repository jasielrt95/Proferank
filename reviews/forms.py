from django import forms
from .models import Review
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["difficulty", "grade", "pro_student", "organized"]

    def save_form(self, user, course, professor):
        r = self.save(commit=False)
        r.user = user
        r.course = course
        r.professor = professor
        r.save()

    
    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.form_action = "rate_professor"
        self.helper.add_input(Submit("submit", "Rate Professor"))

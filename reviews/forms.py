from django import forms
from .models import Review
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["difficulty", "grade", "pro_student", "organized"]

    def save(self, user, course, professor, commit=True):
        review = super(ReviewForm, self).save(commit=False)
        review.user = user
        review.course = course
        review.professor = professor
        if commit:
            review.save()

        return review

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.form_action = "rate_professor"
        self.helper.add_input(Submit("submit", "Rate Professor"))

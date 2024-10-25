from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Password')
    confirm_password = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')

    class Meta:
        model = User
        fields = ['username']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise ValidationError("Passwords do not match.")

class CollegeRegistrationForm(forms.Form):
    COLLEGE_TYPE_CHOICES = [
        ('public', 'Public'),
        ('private', 'Private'),
    ]

    COURSE_CHOICES = [
        ('B.Tech in Computer Science and Engineering', 'B.Tech in Computer Science and Engineering'),
        ('B.Tech in Electrical Engineering', 'B.Tech in Electrical Engineering'),
        ('B.Tech in Mechanical Engineering', 'B.Tech in Mechanical Engineering'),
        ('B.Tech in Civil Engineering', 'B.Tech in Civil Engineering'),
        ('B.Tech in Chemical Engineering', 'B.Tech in Chemical Engineering'),
        ('B.Tech in Aerospace Engineering', 'B.Tech in Aerospace Engineering'),
        ('B.Tech in Biotechnology', 'B.Tech in Biotechnology'),
        ('B.Tech in Environmental Engineering', 'B.Tech in Environmental Engineering'),
        ('B.Tech in Metallurgical and Materials Engineering', 'B.Tech in Metallurgical and Materials Engineering'),
        ('B.Sc in Physics', 'B.Sc in Physics'),
        ('B.Sc in Chemistry', 'B.Sc in Chemistry'),
        ('B.Sc in Mathematics', 'B.Sc in Mathematics'),
        ('M.Tech in Computer Science and Engineering', 'M.Tech in Computer Science and Engineering'),
        ('M.Tech in Structural Engineering', 'M.Tech in Structural Engineering'),
        ('M.Tech in VLSI Design', 'M.Tech in VLSI Design'),
        ('M.Tech in Thermal Engineering', 'M.Tech in Thermal Engineering'),
        ('M.Sc in Physics', 'M.Sc in Physics'),
        ('M.Sc in Chemistry', 'M.Sc in Chemistry'),
        ('M.Sc in Mathematics', 'M.Sc in Mathematics'),
        ('MBA in General Management', 'MBA in General Management'),
        ('MBA in Operations Management', 'MBA in Operations Management'),
        ('MBA in Information Technology Management', 'MBA in Information Technology Management'),
        ('Ph.D. in various Engineering disciplines', 'Ph.D. in various Engineering disciplines'),
        ('Ph.D. in Science disciplines', 'Ph.D. in Science disciplines'),
    ]

    college_name = forms.CharField(max_length=255, required=True)
    college_type = forms.ChoiceField(choices=COLLEGE_TYPE_CHOICES, required=True)
    contact_no = forms.CharField(max_length=15, required=True)

    # Create a field for each course dropdown
    course_1 = forms.ChoiceField(choices=COURSE_CHOICES, required=True)
    course_2 = forms.ChoiceField(choices=COURSE_CHOICES, required=True)
    course_3 = forms.ChoiceField(choices=COURSE_CHOICES, required=True)
    course_4 = forms.ChoiceField(choices=COURSE_CHOICES, required=True)
    course_5 = forms.ChoiceField(choices=COURSE_CHOICES, required=True)
    course_6 = forms.ChoiceField(choices=COURSE_CHOICES, required=True)
    course_7 = forms.ChoiceField(choices=COURSE_CHOICES, required=True)
    course_8 = forms.ChoiceField(choices=COURSE_CHOICES, required=True)
    course_9 = forms.ChoiceField(choices=COURSE_CHOICES, required=True)
    course_10 = forms.ChoiceField(choices=COURSE_CHOICES, required=True)

# forms.py
from django import forms

class SignInForm(forms.Form):
    username = forms.CharField(max_length=150, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

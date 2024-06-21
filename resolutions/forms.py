from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Resolution
from django.contrib.auth.models import User
from .models import Progress

class ResolutionForm(forms.ModelForm):
    class Meta:
        model = Resolution
        fields = ['title', 'description', 'end_date']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save Resolution'))

class UserRegistrationForm(forms.ModelForm):
    first_name = forms.CharField(max_length=25, required=True)
    last_name = forms.CharField(max_length=25, required=True)
    gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], required=True)
    age = forms.IntegerField(required=True)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password', 'first_name', 'last_name', 'gender', 'age']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', 'Passwords do not match')
        return cleaned_data

class SearchForm(forms.Form):
    query = forms.CharField(max_length=100, label='Search Resolutions')

class ProgressForm(forms.ModelForm):
    class Meta:
        model = Progress
        fields = ['date', 'progress']

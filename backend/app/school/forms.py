from django import forms
from .models import School


class SchoolChangeForm(forms.ModelForm):

    class Meta:
        model = School
        fields = ('principal_email', 'verified', 'email_sent', 'school_name', 'school_address')


class SchoolCreationForm(forms.ModelForm):

    class Meta:
        model = School
        fields = ('principal', 'principal_email', 'verified', 'school_name', 'school_address')

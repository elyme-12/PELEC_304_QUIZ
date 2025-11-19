from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['School_name', 'School_address', 'Honors']

    def class_School_name(self):
        school_name = self.cleaned_data.get('School_name')
        if len (school_name) < 3:
            raise forms.ValidationError('Incomplete')
        return school_name
    
    def class_School_address(self):
        school_address = self.cleaned_data.get('School_name')
        if len (school_address) < 3:
            raise forms.ValidationError('Incomplete')
        return school_address
    
    def class_honor(self):
        school_honor = self.cleaned_data.get('School_name')
        if len (school_honor) < 3:
            raise forms.ValidationError('Incomplete')
        return school_honor
    
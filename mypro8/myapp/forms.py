from django import forms
from myapp.models import Student

class StuForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
        widgets = {
                    'name':forms.TextInput(attrs={'class':'form-control form-control-sm','placeholder': 'username'}),
                    'phone':forms.TextInput(attrs={'class':'form-control form-control-sm','placeholder': 'Email'}),
                    'mail':forms.TextInput(attrs={'class':'form-control form-control-sm','placeholder': 'Phone Number'}),
                    'message':forms.TextInput(attrs={'class':'form-control form-control-sm','placeholder': 'Feedback or Enquiry'}),
                    #'User':forms.Select(attrs={'class':'form-control form-control-sm',}),
                    }

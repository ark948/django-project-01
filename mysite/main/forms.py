from django import forms

# name and id will both have the value of 'your_name'
# form tag and submit button must be provided manually

class NameForm(forms.Form):
    your_name = forms.CharField(label="Your name", max_length=100, min_length=2)
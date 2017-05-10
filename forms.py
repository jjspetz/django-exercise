from django import forms

class ContactMeForm (forms.Form):
    name = forms.CharField(label="Name: ", max_length=100)
    email = forms.EmailField(label="Email: ")
    question = forms.CharField(label="Question:", widget=forms.Textarea)

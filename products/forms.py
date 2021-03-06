from django import forms

class ContactForm(forms.Form):
    email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    phone = forms.CharField(required=False)
    message = forms.CharField(widget=forms.Textarea, required=True)
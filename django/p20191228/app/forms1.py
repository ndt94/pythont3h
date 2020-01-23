from django import forms

class MailForm(forms.Form):
    to_email = forms.CharField(label='To email address')
    subject = forms.CharField()
    content = forms.CharField(required=False, widget=forms.Textarea)

    def clean_to_email(self):
        to_email = self.cleaned_data.get('to_email')
        if '@' not in to_email or '.' not in to_email:
            raise forms.ValidationError('Invalid email')
        return to_email
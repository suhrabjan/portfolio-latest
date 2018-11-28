from django import forms
from django_portfolio import settings
from django.core.mail import send_mail


class ContactForm(forms.Form):
    name = forms.CharField(required=True, label='Your Name (required)')
    email = forms.EmailField(required=True, label='Your Email (required)')
    subject = forms.CharField(required=False, label="Subject")
    content = forms.CharField(widget=forms.Textarea, required=False, label="Your Message")

    def send_email(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        subject = self.cleaned_data['subject']
        content = self.cleaned_data['content']
        content = f'Name: {name}. Email: {email}. \nSubject:{subject}\nContent:\n{content}'
        subject = 'Inquiry From Portfolio!'
        send_mail(subject, content, email, [settings.EMAIL_HOST_USER])

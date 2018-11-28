from django.shortcuts import render
from portfolio.forms import ContactForm
from django.views.generic.edit import FormView
# Create your views here.


def portfolio(request):
    return render(request, 'portfolio/portfolio.html')


def home(request):
    return render(request, 'portfolio/home.html')


class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = '/contact/'

    def form_valid(self, form):

        form.send_email()
        return super().form_valid(form)

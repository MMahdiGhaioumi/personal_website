from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from . import forms


class CreateMessage(CreateView):
    form_class = forms.MessageForm
    template_name = 'home/index.html'
    success_url = reverse_lazy('home:home')

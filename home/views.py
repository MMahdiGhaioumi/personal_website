from typing import Any
from django.contrib.auth import get_user_model
from django.views.generic import TemplateView
from contact import forms
from about_me import models


class HomeView(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        context['my_user'] = get_user_model().objects.last()

        context['services'] = models.Service.objects.all()

        context['skills'] = models.Skill.objects.all()

        context['resume_education'] = models.Resume.objects.filter(place=models.Resume.Place.EDUCATION)
        context['resume_experience'] = models.Resume.objects.filter(place=models.Resume.Place.EXPERIENCE)

        context['form'] = forms.MessageForm()

        return context

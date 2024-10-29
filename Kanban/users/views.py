from django.shortcuts import render
from django.views.generic import DetailView, TemplateView

from users.models import User


class UserDetail(DetailView):
    template_name = 'user_profile.html'
    model = User
    context_object_name = 'user'


from django.shortcuts import render
from django.views import generic
from .models import Lizard

class LizardList(generic.ListView):
    model = Lizard
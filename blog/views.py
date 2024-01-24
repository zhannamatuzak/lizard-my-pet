from django.shortcuts import render
from django.views import generic
from .models import Lizard

class LizardList(generic.ListView):
    model = Lizard
    queryset = Lizard.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/index.html'
    paginate_by = 6
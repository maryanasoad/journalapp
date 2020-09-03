from django.http import HttpResponse
from django.views import View
from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Resource
from django.views.generic import ListView


def view_resources(request, *args, **kwargs):
    context = {'resources': Resource.objects.all()}
    return render(request, 'resource_list.html', context)

#class view_resources(ListView):
 #  model = Resource












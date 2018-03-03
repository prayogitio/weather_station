from django.shortcuts import render
from django.template.response import TemplateResponse
from .models import Reading
from .worker import fetch_data

# Create your views here.
def report(request):
    fetch_data()
    data = Reading.objects.last()
    return render(request, 'station/station.html', { 'data': data })


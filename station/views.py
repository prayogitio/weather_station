from django.shortcuts import render
from django.template.response import TemplateResponse
from .models import Reading

# Create your views here.
def report(request):
    data = Reading.objects.last()
    return render(request, 'station/station.html', { 'data': data })


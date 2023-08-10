from django.shortcuts import render
from django.views import View

from .models import Job


def list_job(request):
    jobs = Job.objects.all()
    return render(request, 'list.html', {'jobs': jobs})
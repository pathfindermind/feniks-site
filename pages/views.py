from django.shortcuts import render
from pages.models import Slider, History


def home(request):
    sliders = Slider.objects.all()
    context = {
        'sliders':sliders
    }
    return render(request, 'pages/base.html',  context, request.FILES)

def history(request):
    histories = History.objects.all()
    context = {
        'histories':histories
    }
    return render(request, 'pages/history.html',  context, request.FILES)

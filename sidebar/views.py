from django.shortcuts import render

# Create your views here.
def sidebar(request):
    sliders = Slider.objects.all()
    context = {
        'sliders':sliders
    }
    return render(request, 'sidebar/base.html',  context, request.FILES)

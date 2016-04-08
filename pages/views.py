from django.shortcuts import render
from pages.models import Slider, History
from pages.models import NewsEntry
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



from django.shortcuts import get_object_or_404, render_to_response



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



def index(request):
    entries = NewsEntry.objects.all()
    paginator = Paginator(entries,5)
    page = request.GET.get('page')
    try:
        entries = paginator.page(page)
    except PageNotAnInteger:
        entries = paginator.page(1)
    except EmptyPage:
        entries = paginator.page(paginator.num_pages)
    return render_to_response('pages/base.html', {'entries': entries}, request.FILES)

def category(request, id, slug):
    category = get_object_or_404(Category, id=id,
                                           slug=slug)
    entries = category.entries.published()
    return render_to_response('news/index.html', {'entries': entries})

def archive_year(request, year):
    entries = NewsEntry.objects.filter(draft=False,
                                       published_at__year=year)
    return render_to_response('news/index.html', {'entries': entries})

def archive_month(request, year, month):
    entries = NewsEntry.objects.filter(draft=False,
                                       published_at__year=year,
                                       published_at__month=month)
    return render_to_response('news/index.html', {'entries': entries})

def archive_day(request, year, month, day):
    entries = NewsEntry.objects.filter(draft=False,
                                       published_at__year=year,
                                       published_at__month=month,
                                       published_at__day=day)
    return render_to_response('news/index.html', {'entries': entries})

def details(request, year, month, day, slug):
    entry = get_object_or_404(NewsEntry, draft=False,
                                         published_at__year=year,
                                         published_at__month=month,
                                         published_at__day=day,
                                         slug=slug)
    return render_to_response('news_details.html', {'entry': entry})

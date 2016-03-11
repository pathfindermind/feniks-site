from news.models import NewsEntry

from django.shortcuts import get_object_or_404, render_to_response


def index(request):
    entries = NewsEntry.objects.published()
    return render_to_response('news/index.html', {'entries': entries}, request.FILES)

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
    return render_to_response('news/details.html', {'entry': entry})

from django.shortcuts import render
from documents.models import Constituent

# Create your views here.
def constituent(request):
    c_documents = Constituent.objects.all()
    context = {
        'c_documents': c_documents
    }
    return render(request, 'documents/constituent.html',  context, request.FILES)

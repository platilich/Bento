from django.shortcuts import render
from core.models import Page, Buttons


# Create your views here.
def home(request):
    page = Page.objects.first()
    buttons = Buttons.objects.all()


    data = {'page': page, 'buttons': buttons}

    return render(request, 'index.html', data)
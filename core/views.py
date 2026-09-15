from django.shortcuts import render
from core.models import Profile, Buttons


# Create your views here.
def home(request):
    profile = Profile.objects.exclude(hide=True).first()
    buttons = Buttons.objects.exclude(hide=True)


    data = {'profile': profile,'buttons': buttons}

    return render(request, 'index.html', data)
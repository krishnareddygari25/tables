from django.shortcuts import render

# Create your views here.
from app.models import *
def topic(request):
    QLTO=Topic.objects.all()
    d={'topics':QLTO}

    return render(request,'topic.html',d)




def webpage(request):
    QLWO=Webpage.objects.all()
    d={'webpage':QLWO}
    return render(request,'webpage.html',d)

def accessrecord(request):
    QLAO=AccessRecord.objects.all()
    d={'accessrecord':QLAO}
    return render(request,'accessrecord.html',d)
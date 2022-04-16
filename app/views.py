from django.shortcuts import render
from app.models import *
from django.db.models.functions import Length
# Create your views here.
def display_topic(request):
    t=Topic.objects.all()
    d={'ts':t}
    return render(request,'display_topics.html',d)

def display_web(request):
    w=Webpage.objects.all()
    
    w=Webpage.objects.filter(topic_name='cricket')
    w=Webpage.objects.exclude(topic_name='Kabbadi')
    w=Webpage.objects.all()[2]
    w=Webpage.objects.order_by('name')
    w=Webpage.objects.order_by(Length('name').desc())
    d={'ws':w}
    return render(request,'display_webpages.html',d)


def dispaly_acessrecords(request):
    a=AccessRecords.objects.all()
    d={'as':a}
    return render(request,'display_Acessrecords.html',d)
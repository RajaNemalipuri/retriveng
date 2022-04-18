from django.shortcuts import render
from app.models import *
from django.db.models.functions import Length
from django.db.models import Q
# Create your views here.
def display_topic(request):
    t=Topic.objects.all()
    d={'ts':t}
    return render(request,'display_topics.html',d)

def display_web(request):
    w=Webpage.objects.all()
    
    #w=Webpage.objects.filter(topic_name='cricket')
    #w=Webpage.objects.exclude(topic_name='Kabbadi')
    #w=Webpage.objects.all()[2]
    #w=Webpage.objects.order_by('name')
    #w=Webpage.objects.order_by(Length('name').desc())
    #w=Webpage.objects.filter(name__startswith='A')
    #w=Webpage.objects.filter(name__endswith='h')
    #w=Webpage.objects.filter(name__contains='h')
    #w=Webpage.objects.filter(topic_name__startswith='F')
    w=Webpage.objects.filter(name__in=('Amy','Tony'))
    w=Webpage.objects.filter(name__regex=r'^[a-zA-Z]{2}n')
    w=Webpage.objects.filter(Q(topic_name='Cricket') | Q(name__startswith='A'))
    d={'ws':w}
    return render(request,'display_webpages.html',d)


def dispaly_acessrecords(request):
    a=AccessRecords.objects.all()
    a=AccessRecords.objects.filter(date='2000-04-25')
    a=AccessRecords.objects.filter(date__year__gte='2000')
    a=AccessRecords.objects.filter(date__year__lt='2000')
    a=AccessRecords.objects.filter(date__year__lte='2000')
    a=AccessRecords.objects.filter(date__day='20')
    a=AccessRecords.objects.filter(date__day__gt='20')
    a=AccessRecords.objects.filter(date__day__gte='20')

    d={'as':a}
    return render(request,'display_Acessrecords.html',d)
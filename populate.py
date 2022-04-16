#creating django environment

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','project18.settings')

#adding features of django

import django
django.setup()

#start creating process on poplation
import random

from faker import Faker
f=Faker()

topics=['cricket','Basket Ball','Kabbadi','Vollyball','Foot Ball']

from app.models import *

def add_topic():
    t=Topic.objects.get_or_create(topic_name=random.choice(topics))[0]
    t.save()
    return t

def add_web(wn,wu):
    t=add_topic()
    w=Webpage.objects.get_or_create(topic_name=t,name=wn,url=wu)[0]
    w.save()
    return w


def add_access(wn,wu,wd):
    w=add_web(wn,wu)
    a=AccessRecords.objects.get_or_create(name=w,date=wd)[0]
    a.save()
def add_data(n):
    for i in range(1,n+1):
        wn=f.first_name()
        wu=f.url()
        wd=f.date()

        add_access(wn,wu,wd)
if __name__=='__main__':
    n=int(input('enter n value'))
    add_data(n)


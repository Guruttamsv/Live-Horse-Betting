from django.shortcuts import render
import random
import csv as c
import datetime
# Create your views here.
dictionary = {}
time_of_execution = datetime.datetime.now()
star = time_of_execution + datetime.timedelta(minutes = 10)

def homepage(request):
    global star
    return render(request,'homepage.html',{'starta':star})
def a (request):
    return render(request,'register.html')
def bro (request):
    a = request.GET['name']
    b = request.GET['ph']
    c = request.GET['id']
    d = request.GET['g']
    e = request.GET['m']
    dictionary['name'] = a
    dictionary['phone_number'] = b
    dictionary['ID_proof'] = c
    dictionary['gender'] = d
    dictionary['money_in_dollars'] = e
    print(dictionary)
    return render(request,'choosehorse.html')
def nightmare (request):
    dictionary['horse_name']="Nightmare"
    print(dictionary)
    return render(request,'timer.html')
def gallopy (request):
    dictionary['horse_name']="Gallopy"
    print(dictionary)
    return render(request,'timer.html')
def thunderbolt (request):
    dictionary['horse_name']="Thunderbolt"
    print(dictionary)
    return render(request,'timer.html')
def stallion (request):
    dictionary['horse_name']="Stallion"
    print(dictionary)
    return render(request,'timer.html')
def writen (request):
    f = open('betters.csv', 'a+')
    x = c.DictWriter(f, fieldnames=['name', 'phone_number', 'ID_proof', 'gender', 'money_in_dollars', 'horse_name'])
    x.writerow(dictionary)
    return render(request, 'homepage.html')
def adminhp (request):
    return render(request, 'admin.html')
def adminnext (request):
    naam = request.GET['name']
    paas = request.GET['password']
    admins={'Sangeeth':'devil','Sarath':'ronaldo','Guruttam':'giya'}
    for i in admins:
        if(i==naam and admins[i]==paas):
           return render(request,'adminnext.html')
def inrace (request):
    return render(request, 'race.html')
def racepage(request):
    p = []
    for i in range(0,4):
        p.append(galgalga())

    return render(request, 'almostover.html', {'heyo':p})
def galgalga():
    d = 0
    i = 0.5
    sp = []
    ti = []
    di = []

    def j(speed, distance):
        distance = distance*speed
        return distance

    def f(a, b):
        speed = random.randint(a, b)
        return speed
    s=0
    e=10
    while (True):
        i +=1
        c = f(s, e)
        s+=5
        e+=5
        d = c * i
        if (d <= 2500):
            sp.append(c//2)
            di.append(d)
            ti.append(i)
            p = [sp, di, ti]
        else:
            d = 2500
            i = i
            sp.append(c//2)
            di.append(d)
            ti.append(i)
            break
    return(p)

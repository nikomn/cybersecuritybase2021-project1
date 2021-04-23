from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.db.models import Q
import json
from myapp.models import Patron, PhoneNumber
from django.db import connection,transaction
    

# Create your views here.

def userDetailsView(request, username):
    print(username)
    patron = Patron.objects.get(username=username)
    numbers = PhoneNumber.objects.filter(owner=patron)
    return render(request, 'pages/patronhome.html', {'patron': patron, 'numbers': numbers})

def userHomeView(request):
    return redirect('home')

def patronManagerView(request):
    return render(request, 'pages/patronmanager.html')

def patronFormView(request):
    return render(request, 'pages/newpatron.html')

def loginFormView(request):
    return render(request, 'pages/login.html')

def logoutFormView(request):
    return render(request, 'pages/logout.html')

def loginView(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    print('Attempting login for user', username, 'with password:', password)
    try:
        patron = Patron.objects.get(username=username)
        if patron.password == password:
            print('Password correct! Logging in...')

            if patron.logged == 'False':
                patron.logged = 'True'
                patron.save()
            return render(request, 'pages/loginok.html')
        else:
            print('Wrong password!')
            return render(request, 'pages/loginfail.html')
    except:
        return render(request, 'pages/loginfail.html')

def logoutView(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    try:
        patron = Patron.objects.get(username=username)
        if patron.password == password:
            if patron.logged == 'True':
                patron.logged = 'False'
                patron.save()
            return render(request, 'pages/logoutok.html')
        else:
            return render(request, 'pages/logoutfail.html')
    except:
        return render(request, 'pages/logoutfail.html')

def addNumberView(request, username):
    username = request.POST.get('owner')
    patron = Patron.objects.get(username=username)
    number = request.POST.get('number')
    info = request.POST.get('info')
    print(patron.pk)
    sql_query = "INSERT INTO myapp_phonenumber (owner_id, number, information) \
        values (" + str(patron.pk) + ", '" + number + "', '" + info + "')"
    #PhoneNumber.objects.raw(sql_query)
    cursor = connection.cursor()
    
    cursor.execute(sql_query)
    
    transaction.commit()

    #PhoneNumber.objects.create(owner=patron, number=number, information=info)
    return redirect('/myapp/patrons/' + username)
    
def addPatronView(request):
    username = request.POST.get('username')
    try:
        patronTest = Patron.objects.get(username=username)
        return render(request, 'pages/newpatronfail.html')
    except:
        password = request.POST.get('password')
        ssn = request.POST.get('ssn')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        address = request.POST.get('address')
        Patron.objects.create(username=username, password=password, ssn=ssn, firstname=firstname, lastname=lastname, address=address)
        return render(request, 'pages/newpatronok.html')


    
    

def index(request):
    patrons = Patron.objects.all()
    #return render(request, 'pages/newpatron.html')
    return render(request, 'pages/index.html', {'patrons': patrons})
    # return render(request, 'pages/index.html')
    # return HttpResponse("Hello, world. You're at the myapp index.")
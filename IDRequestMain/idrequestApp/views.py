from os import *
from pyexpat.errors import messages
from .models import *
import email
from pickle import NONE
from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from idrequestApp.models import Useraccount
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required, permission_required
from .forms import Userreg, registerist, fregisterist

import io
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.colors import *
from django.core.files.storage import FileSystemStorage

from django.http import FileResponse
from PyPDF2 import PdfFileWriter, PdfFileReader

from django.template.loader import get_template
from xhtml2pdf import pisa
from reportlab.lib.pagesizes import letter
from datetime import datetime, date
from reportlab.lib.units import inch
# Create your views here.

#def createreg(request):
#    if request.method == "POST":
#        
#        f_irstname= request.POST['fname']
#        m_iddlename = request.POST['mname']
#        l_astname = request.POST['sname']
#        c_ourse = request.POST['course']
#        i_mage = request.POST['stimageup']
#        c_ontactperson = request.POST['contactper']
#        c_ontactnum = request.POST['contactnum']
#        a_ddress = request.POST['address']
#        s_tudnum = request.POST['studnum']
#        s_ignature = request.POST['signature']
        

#        saveee = registration(firstname1=f_irstname, middlename=m_iddlename,lastname=l_astname,course=c_ourse,imagee=i_mage,conterpersonn=c_ontactperson,contactnum=c_ontactnum,
#        address=a_ddress,studnum=s_tudnum,signature=s_ignature)

#        saveee.save()
#        print(form)
#        print(saveee)
#        print("hahaha")
#        return render(request, "Final Html/registration.html")
    #else:
        #print("hohoho")

    #return render(request, "Final Html/registration.html")
    #return render(request, 'registration.html')

#def all_events(request):
    #reglist = registration.objects.all()
    #return render(request, 'Approval.html', {'reglist': reglist})
#def show(request):

    #regist = registration.objects.all()
    #context ={'regist': regist}
    #return render(request, "Approval.html", context)
def loginto(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username= username, password=password)
        if user is not None and user.Usertype == "S":
            login(request, user)
            return redirect('sidreg')

        elif user is not None and user.Usertype == "F":
            login(request, user)
            return redirect('fidreg')
        
        elif user is not None and user.Usertype == "A":
            login(request, user)
            return redirect('approval')
            
        else:
            return render(request, 'Final Html/Login.html',{
                'error_message' : "Username OR password is incorrect"
            })
    elif request.user.is_authenticated and request.user.Usertype == "S":
        return redirect('sidreg')
    elif request.user.is_authenticated and request.user.Usertype == "F":
        return redirect('fidreg')
    elif request.user.is_authenticated and request.user.Usertype == "A":
        return redirect('approval')
    context = {}
    return render(request, 'Final Html/Login.html', context)
    

def gotologout(request):
    logout(request)
    return redirect('loginto')
def login1(request):
    return render(request, "Final Html/Login.html")

@login_required(login_url='login')
def sidreg(request):
    if request.user.is_authenticated and request.user.Usertype == 'S':
        form =  registerist()
        if request.method == 'POST':
            form = registerist(request.POST, request.FILES)
            if form.is_valid():
                
                form.save()
                return redirect('sidreg')
                
            else:
                messages.success(request, form.errors)
                return redirect('sidreg')

        context = {'form': form}
        return render(request, "Final Html/sregistration.html", context)

    elif request.user.is_authenticated and request.user.Usertype == 'F':
        return redirect('fidreg')
    elif request.user.is_authenticated and request.user.Usertype == 'A':
        return redirect('approval')
    else:
        return redirect('loginto')

@login_required(login_url='login')   
def fidreg(request):
    print("try")
    if request.user.is_authenticated and request.user.Usertype == 'F':
        form =  fregisterist()
        print("Good")
        if request.method == 'POST':
            print("Better")
            form = fregisterist(request.POST, request.FILES)
            print("Best")
            if form.is_valid():
                print("HEHEHE")
                form.save()
                return redirect('fidreg')
                
            else:
                messages.success(request, form.errors)
                return redirect('fidreg')

        context = {'form': form}
        return render(request, "Final Html/fregistration.html", context)

    elif request.user.is_authenticated and request.user.Usertype == 'S':
        return redirect('sidreg')
    elif request.user.is_authenticated and request.user.Usertype == 'A':
        return redirect('approval')
    else:
        return redirect('loginto')

@login_required(login_url='login')
def coid(request):
    if request.user.is_authenticated and request.user.Usertype == 'A':
        return render(request, "Final Html/Creation Of ID.html")
    elif request.user.is_authenticated and request.user.Usertype == 'F':
        return redirect('fidreg')
    elif request.user.is_authenticated and request.user.Usertype == 'S':
        return redirect('sidreg')
    else:
        return redirect('loginto')
    

@login_required(login_url='login')
def pdfcreations(request, pk):
    if request.user.is_authenticated and request.user.Usertype == 'A':
        data = registration.objects.filter(id=pk)
        return render(request, "Final Html/PDF.html", {'data':data})
    elif request.user.is_authenticated and request.user.Usertype == 'F':
        return redirect('fidreg')
    elif request.user.is_authenticated and request.user.Usertype == 'S':
        return redirect('sidreg')
    else:
        return redirect('loginto')


@login_required(login_url='login')
def pdfcreationf(request, pk):
    if request.user.is_authenticated and request.user.Usertype == 'A':
        data = Fregistration.objects.filter(id=pk)
        return render(request, "Final Html/fPDF.html", {'data':data})
    elif request.user.is_authenticated and request.user.Usertype == 'F':
        return redirect('fidreg')
    elif request.user.is_authenticated and request.user.Usertype == 'S':
        return redirect('sidreg')
    else:
        return redirect('loginto')
    

@login_required(login_url='login')
def approval(request):
    if request.user.is_authenticated and request.user.Usertype == 'A':
        prs = registration.objects.filter(status = "P")
        prsa = registration.objects.filter(status = "A")
        context = {'prs':prs, 'prsa':prsa}
        return render(request, "Final Html/Approval.html", context)

    elif request.user.is_authenticated and request.user.Usertype == 'F':
        return redirect('fidreg')
    elif request.user.is_authenticated and request.user.Usertype == 'S':
        return redirect('sidreg')
    else:
        return redirect('loginto')

def approvesa(request, id):
    a = registration.objects.get(id=id)
    for x in registration.objects.only('id').filter(status= "P"):
        if a == x:
            x = registration.objects.filter(id=id).update(status="A")
            break
    messages.success(request, "Successfully done")
    return redirect('approval')

@login_required(login_url='login')
def approvalf(request):
    if request.user.is_authenticated and request.user.Usertype == 'A':
        prf = Fregistration.objects.filter(fstatus = "P")
        prfa = Fregistration.objects.filter(fstatus = "A")
        context = {'prf':prf, 'prfa':prfa}
        return render(request, "Final Html/Approvalf.html", context)

    elif request.user.is_authenticated and request.user.Usertype == 'F':
        return redirect('fidreg')
    elif request.user.is_authenticated and request.user.Usertype == 'S':
        return redirect('sidreg')
    else:
        return redirect('loginto')

def approvefa(request, id):
    a = Fregistration.objects.get(id=id)
    for x in Fregistration.objects.only('id').filter(fstatus= "P"):
        if a == x:
            x = Fregistration.objects.filter(id=id).update(fstatus="A")
            break
    messages.success(request, "Successfully done")
    return redirect('approvalf')

def userreg(request):
    form = Userreg()
    if request.method == "POST":
        form = Userreg(request.POST)
        if form.is_valid():
            form.save()
            return redirect('userreg')
        
    context = {'form':form}
    return render(request, "Final Html/userreg.html", context)



@login_required(login_url='login')
def changepass(request):
    return render(request, "Final Html/changepass.html")

def delete(request, pk):
    prs = registration.objects.get(id=pk)
    if request.method == "POST":
        prs.delete()
        return redirect('approval')

    context = {'item':prs}
    return render(request, "Final Html/declinereq.html", context)

def deletef(request, pk):
    prf = Fregistration.objects.get(id=pk)
    if request.method == "POST":
        prf.delete()
        return redirect('approvalf')

    context = {'item':prf}
    return render(request, "Final Html/fdeclinereq.html", context)

def dones(request, pk):
    prsa = registration.objects.get(id=pk)
    if request.method == "POST":
        prsa.delete()
        return redirect('approval')

    context = {'item':prsa}
    return render(request, "Final Html/dones.html", context)

def donef(request, pk):
    prfa = Fregistration.objects.get(id=pk)
    if request.method == "POST":
        prfa.delete()
        return redirect('approvalf')

    context = {'item':prfa}
    return render(request, "Final Html/donef.html", context)

def update(request, pk):
    data = registration.objects.get(id=pk)
    form = registerist(instance = data)
    if request.method == "POST":
        form = registerist(request.POST, request.FILES, instance=data)
        if form.is_valid():
            form.save()
            return redirect('approval')

    context = {'form': form}
    return render(request, "Final Html/supreg.html", context)

def updatef(request, pk):
    data = Fregistration.objects.get(id=pk)
    form = fregisterist(instance = data)
    if request.method == "POST":
        form = fregisterist(request.POST, request.FILES, instance=data)
        if form.is_valid():
            form.save()
            return redirect('approvalf')

    context = {'form': form}
    return render(request, "Final Html/fupreg.html", context)

def new(request, pk):
    data = registration.objects.filter(id=pk)
    return render(request, "Final Html/new.html", {'data':data})

@login_required(login_url='login')
def sview(request, pk):
    if request.user.is_authenticated and request.user.Usertype == 'A':
        data = registration.objects.filter(id=pk)
        return render(request, "Final Html/sview.html", {'data':data})
    elif request.user.is_authenticated and request.user.Usertype == 'F':
        return redirect('fidreg')
    elif request.user.is_authenticated and request.user.Usertype == 'S':
        return redirect('sidreg')
    else:
        return redirect('loginto')

@login_required(login_url='login')
def fview(request, pk):
    if request.user.is_authenticated and request.user.Usertype == 'A':
        data = Fregistration.objects.filter(id=pk)
        return render(request, "Final Html/fview.html", {'data':data})
    elif request.user.is_authenticated and request.user.Usertype == 'F':
        return redirect('fidreg')
    elif request.user.is_authenticated and request.user.Usertype == 'S':
        return redirect('sidreg')
    else:
        return redirect('loginto')
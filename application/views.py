from telnetlib import LOGOUT
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
import pandas
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


# Create your views here.
def home(request):
    return render(request,"index.html")

def signup(request):
    if request.method == "POST":
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        password=request.POST['password']

        myuser=User.objects.create_user(username,email,password)
        myuser.first_name=fname
        myuser.last_name=lname

        return redirect('signin')

    return render(request,"signup.html")

def signin(request):
    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['password']

        user=authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            username= user.get_username
            return render(request,"Homep.html",{'username':username})
        else:
            messages.error(request,"Wrong Credentials")
            return redirect('home')
    return render(request,"signin.html")

def signout(request):
    logout(request)
    return redirect('home')

def Homep(request):
    return render(request,"Homep.html")

def Hospitals(request):
    return render(request,"Hospitals.html")

def diet(request):
    return render(request,"diet.html")

def prediction(request):
     return render(request,"prediction.html")  
def explore(request):
    return render(request,"explore.html")  

def prediction1(request):
     data = pandas.read_csv("C:\diabetes.csv")
     X = data.drop("Outcome", axis=1)
     Y = data["Outcome"]
     X_train, X_test , Y_train , Y_test =train_test_split(X, Y, test_size=0.2,random_state=42)
     model = LogisticRegression()
     model.fit(X_train, Y_train)

     value1=float(request.POST['n1'])
     value2=float(request.POST['n2'])
     value3=float(request.POST['n3'])
     value4=float(request.POST['n4'])
     value5=float(request.POST['n5'])
     value6=float(request.POST['n6'])
     value7=float(request.POST['n7'])
     value8=float(request.POST['n8'])

     result=model.predict([[value1,value2,value3,value4,value5,value6,value7,value8]])
     result1 = ""
     if result==[1]:
        result1="You might be diabetic.Consult a physician"
     else:
        result1="You are not diabetic"

     return render(request,"prediction.html",{"output":result1})
def cp(request):
    return render(request,"cp.html")
def cp1(request):
     data = pandas.read_csv("C:\cancer.csv")
     X = data.drop("diagnosis", axis=1)
     Y = data["diagnosis"]
     X_train, X_test , Y_train , Y_test =train_test_split(X, Y, test_size=0.2,random_state=42)
     model = LogisticRegression()
     model.fit(X_train, Y_train)

     value1=float(request.POST['n0'])
     value2=float(request.POST['n1'])
     value3=float(request.POST['n2'])
     value4=float(request.POST['n3'])
     value5=float(request.POST['n4'])
     value6=float(request.POST['n5'])
     value7=float(request.POST['n6'])
     value8=float(request.POST['n7'])
     value9=float(request.POST['n8'])
     value10=float(request.POST['n9'])
     value11=float(request.POST['n10'])
     value12=float(request.POST['n11'])
     value13=float(request.POST['n12'])
     value14=float(request.POST['n13'])
     value15=float(request.POST['n14'])
     value16=float(request.POST['n15'])
     value17=float(request.POST['n16'])
     value18=float(request.POST['n17'])
     value19=float(request.POST['n18'])
     value20=float(request.POST['n19'])
     value21=float(request.POST['n20'])
     value22=float(request.POST['n21'])
     value23=float(request.POST['n22'])
     value24=float(request.POST['n23'])
     value25=float(request.POST['n24'])
     value26=float(request.POST['n25'])
     value27=float(request.POST['n26'])
     value28=float(request.POST['n27'])
     value29=float(request.POST['n28'])
     value30=float(request.POST['n29'])
     result=model.predict([[value1,value2,value3,value4,value5,value6,value7,value8,value9,value10,
                            value11,value12,value13,value14,value15,value16,value17,value18,value19,value20,
                            value21,value22,value23,value24,value25,value26,value27,value28,value29,value30,]])
     result1 = ""
     if result==['M']:
        result1="You may have breast cancer . Consult the doctor."
     else:
        result1="You don't have breast cancer."

     return render(request,"cp.html",{"output":result1})     
def Ananthapur(request):
    return render(request,"Ananthapur.html")
def Chittoor(request):
    return render(request,"Chittoor.html")
def EastGodhavari(request):
    return render(request,"EastGodhavari.html")
def Guntur(request):
    return render(request,"Guntur.html")
def Kadapa(request):
    return render(request,"Kadapa.html")
def Krishna(request):
    return render(request,"Krishna.html")
def Kurnool(request):
    return render(request,"Kurnool.html")
def Nellore(request):
    return render(request,"Nellore.html")
def Prakasam(request):
    return render(request,"Prakasam.html")
def Srikakulam(request):
    return render(request,"Srikakulam.html")
def Vijayanagaram(request):
    return render(request,"Vijayanagaram.html")
def Visakhapatnam(request):
    return render(request,"Visakhapatnam.html")
def WestGodhavari(request):
    return render(request,"WestGodhavari.html")
from django.shortcuts import render,redirect
from .forms import CustomerForm
from .models import Customer
from django.http import HttpResponseRedirect


# Create your views here.


def home(request):
    customers = Customer.objects.all()
    frontend_stuff = {}
    return render(request,"home.html",frontend_stuff)

def check_bmi(request):
      form = CustomerForm()
      if request.method == "POST":
             form = CustomerForm(request.POST)
             if form.is_valid():
              form.save()
              return redirect("/result")
      frontend_stuff = {"form":form}
      return render(request,"check_bmi.html",frontend_stuff)


def result(request):
      customers = Customer.objects.all()
      pre_obesity_count = 0
      underweight_count = 0
      NormalWeight_count = 0
      moderate_risk_count = 0
      high_risk_count = 0
      low_risk_count=0
      total = customers.count()
      for customer in customers:
            bmi = customer.get_bmi
            customer_id = customer
            height = customer.height
            weight = customer.weight
            if bmi < 18.5:
                  message = "Under Weight"
                  underweight_count+=1
                  color = "light green "
            elif bmi >= 18.5 and bmi <= 24.9:
                  message = "Normal  Weight"
                  NormalWeight_count+=1
                  color = "green"
            elif bmi >= 25 and bmi <= 29.9:
                  message = "Pre-Obesity"
                  pre_obesity_count+=1
                  color = "orange"
            elif bmi >= 30 and bmi <= 34.9:
                  message = "Low Risk Obesity"
                  low_risk_count+=1
                  color = "dark orange"
            elif bmi >= 35 and bmi <= 39.9:
                  message = "Moderate Risk Obesity"
                  moderate_risk_count+=1
                  color = "red"
            elif bmi >= 40:
                  message = "High Risk Obesity"
                  high_risk_count+=1
                  color = "dark red" 
      frontend_stuff = {"bmi":bmi,"message":message,"total":total,"highobesity":high_risk_count,
      "lowobesity":low_risk_count,"moderateobesity":moderate_risk_count,"normal":NormalWeight_count,
      "underweight":underweight_count,"preobesity":pre_obesity_count,}
      return render(request,"result.html",frontend_stuff)


def about(request):
      frontend_stuff={}
      return render(request,"aboutBmi.html",frontend_stuff)








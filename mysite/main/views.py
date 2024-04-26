from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from main.forms import NameForm
from icecream import ic

# Create your views here.

def index(request):
    return render(request, "main/index.html")

def login(request):
    return render(request, "main/login.html")

def send_data_by_form(request):
    return render(request, "main/form_test.html")

def get_data_by_form(request):
    if request.method == "POST":
        name = request.POST.get("name")
        print(name)
        
    return render(request, "main/form_data.html", {"name": name})

def test_django_form(request):
    context = {}
    context["error"] = None
    context["form"] = NameForm()
    if request.method == "POST":
        form = NameForm(request.POST)
        if form.is_valid():
            context["name"] = form.cleaned_data["your_name"]
            return render(request, "main/django_form.html", context=context)
        else:
            context["error"] = "form was not validated."
    return render(request, "main/django_form.html", context=context)
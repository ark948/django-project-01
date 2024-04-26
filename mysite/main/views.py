from django.shortcuts import render

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
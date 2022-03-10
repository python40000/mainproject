from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.core.mail import send_mail
# from Home.models import Faculty
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from Home.models import Faculty
from mainproject.settings import EMAIL_HOST_USER

# Create your views here.

def home(request):
    return render(request, 'homepage.html')

def show(request):
    obj  = Faculty.objects.all()
    return render(request, 'show.html', {"obj":obj})

def reg(request):
    if request.method == "GET":
        return render(request, "reg_form.html")
    else:

        id = request.POST.get("id")
        name = request.POST.get("name")
        place = request.POST.get("place")
        position = request.POST.get("position")
        email = request.POST.get("email")
        password = request.POST.get("password")
        Faculty.objects.create(faculty_id=id,faculty_name=name,faculty_place=place,faculty_position=position,faculty_email=email,faculty_password=password)
        User.objects.create_user(id=id,username=name,password=password,email=email)

        send_mail(
            "FLIPKART",
            "Registered Successfully",
            EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )

        return redirect('Home:show')

def delete(request, fid):
    Faculty.objects.get(faculty_id=fid).delete()
    return redirect('Home:show')

def edit(request, fid):
    if request.method == "GET":
        obj = Faculty.objects.get(faculty_id=fid)
        return render(request, 'edit.html', {"obj":obj})
    else:
        uid = request.POST.get("id")
        name = request.POST.get("name")
        place = request.POST.get("place")
        email = request.POST.get("email")
        position = request.POST.get("position")
        password = request.POST.get("password")
        Faculty.objects.filter(faculty_id=fid).update(faculty_id=uid,faculty_name=name,faculty_place=place,faculty_position=position,faculty_email=email,faculty_password=password)
        User.objects.filter(id=fid).update(username=name,email=email,password=password)

        send_mail(
            "FLIPKART",
            "Details Updated",
            EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )

        return redirect('Home:show')

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        uname = request.POST.get("uname")
        password = request.POST.get("password")
        user = authenticate(username=uname, password=password)
        if user is not None:
            return HttpResponse("success")
        else:
            return HttpResponse("fail")
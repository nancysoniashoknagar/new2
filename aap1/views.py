from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from aap1.models import Student,Games

def home(request):
    return HttpResponse("Hello world")
    
def profile(request):
    return HttpResponse("Student Registration page")
    
def a(request):
    if request.method == 'POST':
        global name
        name = request.POST.get('name')
        rollno = request.POST.get('rollno')
        phone = request.POST.get('phone')
        students = Student(name=name, rollno=rollno, phone=phone)
        students.save()
    return render(request, "a.html")



    
def c(request):
    if request.method == 'POST':
        global point
        gamename = request.POST.get('gamename')
        point = request.POST.get('point')
        game = Games(gamename=gamename, point=point )
        game.save()
    return render(request, "c.html")
# Create your views here.


def b(request):
    from aap1.models import Student
    from aap1.models import Games
    rec= Student.objects.filter(name=name)
    gec= Games.objects.filter(point=point)
    print(gec)
    return render(request,"b.html",{'rec':rec},{'gec':gec})


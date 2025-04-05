from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "index.html")

def member(request):
    return render(request, "member.html")

def form(request):
    return HttpResponse("<h1>แบบฟอร์มบันทึกข้อมูล</h1>")

def academic(request):
    return render(request, "academic.html")
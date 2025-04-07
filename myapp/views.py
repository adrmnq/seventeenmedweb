from django.shortcuts import render
from django.http import HttpResponse
import json

with open("hello_world/static/members/members.json") as f:
    member_contents = json.load(f)
with open("hello_world/static/academic/academic.json") as a:
    academic_contents = json.load(a)

for order in member_contents['treasurer']:
    print(order['id'])
# Create your views here.
def index(request):
    name = "adrmnq"
    age = 20
    return render(request, "index.html", {"name":name, "age":age})

def member(request):
    return render(request, "member.html", member_contents)

def form(request):
    return HttpResponse("<h1>แบบฟอร์มบันทึกข้อมูล</h1>")

def academic(request):
    return render(request, "academic.html", academic_contents)

def login(request):
    return render(request, "login.html")
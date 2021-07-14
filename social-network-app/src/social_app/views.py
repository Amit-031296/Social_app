from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_view(request):
    user = request.user
    hello = "Welcome To Social App"
    context = {
        'user':user,
        'hello':hello}
    return render(request,'main/home.html',context)
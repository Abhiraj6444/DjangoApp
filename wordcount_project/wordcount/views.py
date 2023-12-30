from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request, 'home.html', { 'messageonpage' : "This my first webpage with you" })

def eggs(request):
    return HttpResponse('<H1>EGGS<H1>')
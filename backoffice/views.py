from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'backoffice/dashboard.html')

def get_orders(request):
    return HttpResponse("Hello, world. You're at the blist of orders.")




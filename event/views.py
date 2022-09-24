from multiprocessing import context
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Events
from .forms import Event

# Create your views here.
def home(request):
    context = {}
    context["dataset"]= Events.objects.all()
    return render(request,'index.html',context)

def create(request):
    if request.method == 'POST' :
        Task = Event(request.POST, request.FILES)
        if Task.is_valid():
            Task.save()
            return redirect('/')
    else:
        Task = Event()
        return render(request,'create.html',{'form':Task})

def detail_view(request,id):
    context={}
    context["data"] = Events.objects.get(id= id)
    return render(request,'detail.html',context)
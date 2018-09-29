from django.shortcuts import render
import datetime




def home (request):
    time = datetime.datetime.now()
    context = {
        "time":time
    }
    template_name = "home.html"
    return render(request,template_name,context)


def base(request):
    time = datetime.datetime.now()
    context = {
        "time":time
    }
    template_name ="base.html"
    return render(request,template_name,context)
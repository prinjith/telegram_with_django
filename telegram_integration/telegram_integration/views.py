from django.shortcuts import render
# from django.http import HttpResponse, JsonResponse

def index(request):
    # return HttpResponse(index.html)
    return render(request,'index.html')
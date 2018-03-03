from django.shortcuts import render

def homepage(request):
    # return HttpResponse('Homepage')
    return render(request, 'homepage.html')
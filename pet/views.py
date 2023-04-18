from django.shortcuts import render 


def pet(request):
    return render(request, 'pet/index.html')
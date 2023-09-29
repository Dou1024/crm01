from django.shortcuts import render, HttpResponse, reverse, redirect


def son2(request):
    print("app_01")
    return render(request, 'app02/index.html', {"name": "doudou"})
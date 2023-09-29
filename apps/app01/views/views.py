import datetime
from django.shortcuts import render, HttpResponse, reverse, redirect


# Create your views here.

def app_01(request):
    print("app_01")
    # return HttpResponse("app_01")
    context = {
        "n1": "豆豆",
        "n2": [1, 2, 3],
        "n3": {
            "name": "jack",
            "age": "16",
            "sex": "man"
        },
        "n4": "",
        "n8": "xiaodou",
        "n9": datetime.datetime.utcnow() + datetime.timedelta(hours=8),
        "n10": datetime.datetime.now().strftime("%Y-%m-%d:%H:%I:%S"),
        "n11": [
            {"id": 1, "name": "dou1", "age": 16},
            {"id": 2, "name": "dou2", "age": 18},
            {"id": 3, "name": "dou3", "age": 25},
        ],
        "n12": "",
    }
    return render(request, 'app01/index.html', context)


def son(request):
    url = reverse("app01:son")
    # url = redirect("app02:son2")
    print(url)
    content = {
        "info1": "hello",
        "info2": "how are you.",
        "info3": "这是block里面的",
        "url": url,
    }
    return render(request, "app01/son.html", content)


def user(request):
    print("函数")
    # int("shdif")    # 异常捕获
    # print(request.resolver_match)
    return render(request, "index.html")

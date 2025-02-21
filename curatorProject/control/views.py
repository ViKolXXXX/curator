from django.http import HttpResponse, HttpResponseServerError
from django.shortcuts import render


def index(request):
    # data = {"header": "Hello Django", "message": "Welcome to Python"}
    return render(request, "index.html")
    # return render(request, "index.html", context=data)

def create_event(request):
    print(request.POST)
    return HttpResponse("<h2>Создать событие</h2>")

def about(request, name, age):
    return HttpResponse(f"""
            <h2>О пользователе</h2>
            <p>Имя: {name}</p>
            <p>Возраст: {age}</p>
    """)

def contact(request):
    return HttpResponseServerError("Server Error")

def user(request, name="Undefined", age =0):
    return HttpResponse(f"<h2>Имя: {name}  Возраст: {age}</h2>")


def products(request, id):
    return HttpResponse(f"Товар {id}")

def comments(request, id):
    return HttpResponse(f"Комментарии о товаре {id}")

def questions(request, id):
    return HttpResponse(f"Вопросы о товаре {id}")


def userss(request):
    age = request.GET.get("age")
    name = request.GET.get("name")
    return HttpResponse(f"<h2>Имя: {name}  Возраст: {age}</h2>")
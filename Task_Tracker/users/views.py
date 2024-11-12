
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import RegistrationForm, LoginForm
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Profile
from .serializers import ProfileSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def profile_list(request, format=None):
    if request.method == 'GET':
        snippets = Profile.objects.all()
        serializer = ProfileSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProfileSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def profile_detail(request, pk, format=None):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Profile.objects.get(pk=pk)
    except Profile.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ProfileSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ProfileSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)


def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        print("проверка на метод")
        if form.is_valid():
            form.save()
            print('Форму сохранили в БД')
            return redirect('login')
        else:
            print("форма невалидна")

    else:
        form = RegistrationForm()


    context = {'form': form}
    return render(request, 'signup.html', context)



def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        print('проверка на метод')

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                print('шалость удалась')
                return redirect('http404')
            else:
                form.add_error(None, 'Неверный логин или пароль')
                print("неверный логин или пароль")
        else:
            print('Неправильно заполнена форма')

    else:
        form = LoginForm()

    context = {'form': form}
    return render(request, 'signin.html', context)


def http404(request):
    return render(request, '404.html')

def main(request):
    return render(request, 'main.html')
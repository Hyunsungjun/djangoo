from django.urls import reverse
from django.http.response import HttpResponseRedirect
from accountapp.models import HelloWolrd
from django.shortcuts import render


def hello_world(request):
    if request.method == "POST":
        temp = request.POST.get('hello_world_input')

        new_hello_world = HelloWolrd()
        new_hello_world.text = temp
        new_hello_world.save()

        return HttpResponseRedirect(reverse('accountapp:hello_world'))
    else:
        hello_world_list = HelloWolrd.objects.all()
        return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})
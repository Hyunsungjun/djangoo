from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse, reverse_lazy
from django.http.response import HttpResponseRedirect
from accountapp.models import HelloWolrd
from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.models import User


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


class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/create.html'

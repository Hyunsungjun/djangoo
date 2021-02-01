from accountapp.views import AccountCreateView, hello_world
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

app_name = "accountapp"  # 한번에 리디렉트

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world')  # name
    , path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('create/', AccountCreateView.as_view(), name='create')
]

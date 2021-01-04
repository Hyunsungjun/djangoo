from django.urls import path
from accountapp.views import hello_world

app_name = "accountapp"  # 한번에 리디렉트

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world')  # name 라우트에 대한 이름
]

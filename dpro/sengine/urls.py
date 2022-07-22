from django.urls import path, include
from sengine.views import *

urlpatterns = [
    path('index/', index, name='main-view'),
    path('', MyCreateView.as_view(), name='main-view1'),
    path('login', LoginView.as_view(), name='login'),
]
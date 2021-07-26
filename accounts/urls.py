from django.urls import path, include
from .views import Signin, signup, home


urlpatterns = [
    path('home/', home, name='home'),
    path('login/', Signin, name='login'),
    path('signup/', signup, name='signup'),
]

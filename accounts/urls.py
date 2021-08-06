from django.urls import path, include
from .views import Signin, signup, user_logout


urlpatterns = [
    path('login/', Signin, name='login'),
    path('signup/', signup, name='signup'),
    path('logout/', user_logout, name='logout'),
]

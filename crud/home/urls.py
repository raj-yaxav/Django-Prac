# card/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('signup/', signup , name="signup"),
    path('login/' , login_view , name="login"),
    path('logout/', logout_view , name = "logout"),
    path('create/', createCard, name='create'),

    path('update/<int:id>/', updateCard, name='update'),
    path('delete/<int:id>/', deleteCard, name='delete'),
]
from django.urls import path
from .views import *

urlpatterns = [
    path('login/', mylogin, name='login'),
    path('register/', myregister, name='register'),
    path('logout/', mylogout, name='logout'),
    path('forgot/', forgot, name='forgot'),

    path('', home, name='home'),
    path('profile/', profile, name='profile'),
    path('article/<int:id>', article, name='article'),
    path('categorie/<int:id>/<int:n>/', categorie, name='categorie'),
]

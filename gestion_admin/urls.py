from django.urls import path
from .views import *

urlpatterns = [
    path('profiles/<int:n>', profiles, name='profiles'),
    path('articles/<int:n>', articles, name='articles'),
    path('categories/<int:n>', categories, name='categories'),
    path('niveaux/<int:n>', niveaux, name='niveaux'),
    path('historique/<int:n>', historique, name='historique'),

    path('profile/<int:id>', update_profile, name='profile_edit'),
    path('article/<int:id>', update_article, name='article_edit'),
    path('categorie/<int:id>', update_categorie, name='categorie_edit'),
    path('niveau/<int:id>', update_niveau, name='niveau_edit'),

    path('article/', create_article, name='create_article'),
    path('categorie/', create_categorie, name='create_categorie'),
    path('niveau/', create_niveau, name='create_niveau'),
    

]

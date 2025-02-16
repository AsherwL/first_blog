from django.urls import path
from .views import accueil, articles_par_categorie, detail_article, recherche_articles, a_propos, contact

urlpatterns = [
    path('', accueil, name='accueil'),
    path('categorie/<str:categorie>/', articles_par_categorie, name='articles_par_categorie'),
    path('article/<int:article_id>/', detail_article, name='detail_article'),
    path('recherche/', recherche_articles, name='recherche_articles'),  # Route pour la recherche
    path('a-propos/', a_propos, name='a_propos'),  # URL pour la page À Propos
    path('contact/', contact, name='contact'),  # URL pour la page Contact
]

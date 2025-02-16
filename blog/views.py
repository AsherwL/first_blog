from lib2to3.fixes.fix_input import context

from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from unicodedata import category

from blog.models import Article


def accueil(request):
    """ Affiche la page d'accueil avec un menu et les derniers articles """
    categories = [
        ('livres', 'Livres'),
        ('plume', 'Plume'),
        ('meditations', 'Méditations'),
        ('anime_musique_series', 'Animé musique & séries'),
    ]
    articles_recents = Article.objects.all().order_by('-date_publication')[:5]
    return render(request, "blog/accueil.html", {'categories': categories, 'articles_recents': articles_recents})

def articles_par_categorie(request, categorie):
    """ Affiche les articles d'une catégorie avec pagination """
    articles_list = Article.objects.filter(categorie=categorie).order_by('-date_publication')

    # Pagination : 5 articles par page
    paginator = Paginator(articles_list, 5)
    page_number = request.GET.get('page')  # Récupère le numéro de la page dans l'URL
    articles = paginator.get_page(page_number)  # Récupère les articles de la page demandée

    return render(request, "blog/articles_par_categorie.html", {'articles': articles, 'categorie': categorie})

def detail_article (request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, "blog/detail_article", context={"article": article})


def recherche_articles(request):
    """ Recherche d'articles avec pagination """
    query = request.GET.get("q", "")
    articles_list = Article.objects.filter(Q(titre__icontains=query) | Q(contenu__icontains=query)) if query else []

    # Pagination : 5 résultats par page
    paginator = Paginator(articles_list, 5)
    page_number = request.GET.get('page')
    articles = paginator.get_page(page_number)

    return render(request, "blog/recherche.html", {"articles": articles, "query": query})

def a_propos(request):
    """ Affiche la page À Propos """
    return render(request, "blog/a_propos.html")

def contact(request):
    """ Affiche la page Contact """
    return render(request, "blog/contact.html")

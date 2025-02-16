from django.db import models

# Create your models here.
class Article(models.Model):
    CATEGORY_CHOICES = [
        ('lecture','Lectures'),
        ('plume', 'Plume'),
        ('meditations', 'Méditations'),
        ('Anime_musique_series','Animé musique & séries '),
    ]

    titre = models.CharField(max_length=255)
    categorie = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    contenu = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    date_publication = models.DateField(auto_now=True)
    lien_video = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.titre
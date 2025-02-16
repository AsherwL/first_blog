from django.contrib import admin
from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('titre', 'categorie', 'date_publication', 'image_present')  # Ajout d'un indicateur d'image
    list_filter = ('categorie', 'date_publication')
    search_fields = ('titre', 'contenu')
    ordering = ('-date_publication',)  # Trie par date décroissante
    date_hierarchy = 'date_publication'  # Barre de navigation par dates

    fieldsets = (
        ('Informations Générales', {
            'fields': ('titre', 'categorie', 'image', 'lien_video')
        }),
        ('Contenu', {
            'fields': ('contenu',)
        }),
        ('Détails', {
            'fields': ('date_publication',)
        }),
    )

    readonly_fields = ('date_publication',)  # Empêche la modification de la date

    def image_present(self, obj):
        return "✅" if obj.image else "❌"  # Affiche un ✅ si une image est ajoutée
    image_present.short_description = "Image"

admin.site.site_header = "Gestion du Blog - Asher"
admin.site.site_title = "Mon Blog Admin"
admin.site.index_title = "Bienvenue dans l'espace d'administration"

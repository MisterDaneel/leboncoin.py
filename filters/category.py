# Category in which to search
#
# category_id category_name
#  2          Voitures
#  3          Motos
#  4          Caravaning
#  5          Utilitaires
#  6          Équipement auto
#  7          Nautisme
#  9          Ventes immobilières
# 10          Locations
# 11          Colocations
# 12          Locations & Gîtes
# 13          Bureaux & Commerces
# 15          Informatique
# 16          Image & Son
# 17          Téléphonie
# 19          Ameublement
# 20          Électroménager
# 21          Bricolage
# 22          Vêtements
# 23          Équipement bébé
# 25          DVD - Films
# 26          CD - Musique
# 27          Livres
# 28          Animaux
# 29          Sports & Hobbies
# 30          Instruments de musique
# 32          Équipements industriels
# 33          Offres d'emploi",
# 34          Prestations de services
# 35          Billetterie
# 36          Cours particuliers
# 38          Autres
# 39          Décoration
# 40          Collection
# 41          Jeux & Jouets
# 42          Montres & Bijoux
# 43          Consoles & Jeux vidéo
# 44          Équipement moto
# 45          Arts de la table
# 46          Linge de maison
# 47          Accessoires & Bagagerie
# 48          Vins & Gastronomie
# 49          Évènements
# 50          Équipement caravaning
# 51          Équipement nautisme
# 52          Jardinage
# 53          Chaussures
# 54          Vêtements bébé
# 55          Vélos
# 57          Matériel agricole
# 58          Transport - Manutention
# 59          BTP - Chantier gros-oeuvre
# 60          Outillage - Matériaux 2nd-oeuvre
# 61          Restauration - Hôtellerie
# 62          Fournitures de bureau
# 63          Commerces & Marchés
# 64          Matériel médical
# 65          Covoiturage
# 67          Chambres d'hôtes
#


def category(filters):
    if "category" in filters:
        return {
            "id": str(filters["category"])
        }
    return {}

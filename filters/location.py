# The location of the offer
# Only one of departments, region, and city_zipcode is necessary, or it can stay empty
#
# region_name                    region_id
#
#  Alsace                        1
#  Aquitaine                     2
#  Auvergne                      3
#  Basse-Normandie               4
#  Bourgogne                     5
#  Bretagne                      6
#  Centre                        7
#  Champagne-Ardenne             8
#  Corse                         9
#  Franche-Comté                 10
#  Haute-Normandie               11
#  Île-de-France                 12
#  Languedoc-Roussillon          13
#  Limousin                      14
#  Lorraine                      15
#  Midi-Pyrénées                 16
#  Nord-Pas-de-Calais            17
#  Pays de la Loire              18
#  Picardie                      19
#  Poitou-Charentes              20
#  Provence-Alpes-Côte d'Azur    21
#  Rhône-Alpes                   22
#
#
# ZIPCODES EXAMPLE:
# location = {
#     "locations": [
#         {"zipcode": "75018"},
#         {"zipcode": "75019"},
#     ]
# }
#
#
# REGIONID EXAMPLE:
# location = {
#     "locations": [
#       {"region_id":"12"{
#     ]
# }
#


def location(filters):
    if "zipcode" in filters:
        locations = []
        for zipcode in filters["zipcode"]:
            locations.append(
                {"zipcode": zipcode},
            )
        return {"locations": locations}
    return {}

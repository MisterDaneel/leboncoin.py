# range for prices and other
#
#
# ranges = {
#     'price':{
#         'min': 0,
#         'max': 1000000
#     }
# }


def ranges(filters):
    ranges = {}
    if "price" in filters:
        ranges["price"] = filters["price"]
    return ranges

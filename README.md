# Search on leboncoin.fr with python

Based on leboncoin api: https://api.leboncoin.fr

You may have to add api_key to your headers (look HTTP headers from POST requests to api.leboncoin.fr emit by your browser)

Limit is the number of ads to your request.

# Configuration

leboncoin.py looks for a file named config.json.

```
{
    "filters": {
        "zipcode": ["01200", "13780", "37160", "94390"],
        "category": "2",
        "price": {
            "min": 0,
            "max": 500000
        },
        "keywords": ["moteur"]
    },
    "limit": 60,
    "headers": {
        "User-Agent": "Mozilla/5.0 Firefox/62.0",
        "Accept": "*/*",
        "DNT": "1"
    }
}
```


# Filters:

The filters field is optionnal. Each filter is optionnal too.

## zipcode:
A list of zipcodes.
```
"zipcode": ["01200", "13780", "37160", "94390"]
```

## price:
A price range.
```
"price": {
    "min": 0,
    "max": 500000
}
```

## keywords:
A list of keywords to search in title or content.
```
"keywords": ["chat", "chien"]
```

## category:
A category id to filter results. You can found a list of categories in filters/category.py
```
"category": "2"
```

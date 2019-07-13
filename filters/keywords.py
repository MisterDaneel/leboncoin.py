# The search keyword
#
# {"text": "keyword"} or {"text": "keyword", "type": "subject"} in order to search in the title only
#

def keywords(filters):
    keywords = {}
    if "keywords" in filters:
        text = ""
        for keyword in filters["keywords"]:
            text += keyword + " "
        keywords["text"] = text
    return keywords

import requests
from app.fetch_articles_summary import fetch_articles_summary

def fetch_articles(next_page_id, isNextPageAvailable):
    if not isNextPageAvailable:
        api_url = "https://newsdata.io/api/1/latest?apikey=pub_70272cd31c68fc8e897869b07c198e8221baf&removeduplicate=1&prioritydomain=top"
    else:
        api_url = f"https://newsdata.io/api/1/latest?apikey=pub_70272cd31c68fc8e897869b07c198e8221baf&removeduplicate=1&prioritydomain=top&page={next_page_id}"
    
    response = requests.get(api_url)
    data = response.json()
    articles = data.get("results", [])
    next_page = data.get("nextPage", "")

    cleaned_articles = []
    for items in articles:
        i = 1
        summary_url = items.get("link", "")
        print(f"Fetching summary {1}... Please wait.")
        summary = fetch_articles_summary(summary_url)
        ("Summary received.")
        i+=1

        cleaned_article = {
            "article_id": items.get("article_id", ""),
            "title": items.get("title", ""),
            "link": items.get("link", ""),
            "description": items.get("description", ""),
            "pubDate": items.get("pubDate", ""),
            "source": {
                "source_id": items.get("source_id", ""),
                "source_name": items.get("source_name", ""),
                "source_url": items.get("source_url", ""),
                "source_icon": items.get("source_icon", "")
            },
            "language": items.get("language", ""),
            "country": items.get("country", []),
            "category": items.get("category", []),
            "summary": summary,
            "views": 0
        }

        cleaned_articles.append(cleaned_article)

    return cleaned_articles, next_page

from app.fetch_articles import fetch_articles
from app.firestore_utils import store_article

def process_articles():
    next_page_id = ""
    i = 0

    while i < 3:
        print(f"Fetching page {i + 1}...")

        if i == 0:
            articles, next_page = fetch_articles("", False)
        else:
            articles, next_page = fetch_articles(next_page_id, True)

        next_page_id = next_page

        for article in articles:
            print(article)
            store_article(article)

        i += 1

if __name__ == "__main__":
    print("Main start...")
    process_articles()
    print("Main end...")

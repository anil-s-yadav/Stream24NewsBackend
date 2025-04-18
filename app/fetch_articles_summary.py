# fetch_articles_summary
import requests

def fetch_articles_summary(url):
    api_url = "http://127.0.0.1:8000/summarize/"
    #api_url = "https://your-service-name.onrender.com/summarize/"
    
    response = requests.post(api_url, data={"url": url}) 

    if response.status_code == 200:
        data = response.json()
        summary = data.get("summary", "")
        return summary
    else:
        return f"Error: {response.status_code}, {response.text}"

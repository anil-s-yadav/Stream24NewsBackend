call below news api 
https://newsdata.io/api/1/latest?apikey=pub_70272cd31c68fc8e897869b07c198e8221baf&removeduplicate=1&prioritydomain=top

you will get - 
{
"status": "success",
"totalResults": 477649,
"results": [],
"nextPage": "1744755660618160752"
}

result:[] field has all new data.

DB structure - 
collection(news)->doc(article_id)-> then below feilds(map inside result)

"results": [
{
    "article_id": "22f48f095865e9f1070a94f2fb5d242f",
    "title": "Plants, Fungi And Bacteria Working Together - Mirage News",
    "link": "https://news.google.com/rss/articles/CBMihAFBVV95cUxQUHJsS0FzRnM4YU5CakE5RXcwYW9iWTRaeDBIaEZ0akhnazRnVENDZVBSeU5JRmI1OWRIYXNZbHVQRC1rVTByVXdrc3RVMEFUeC1yS1Voem9CZ3dXc3o2b0NzaVY0azhIZERKeGR3YmZUZmgzV1FNVGU4ZVBCcmJPM1N5amI?oc=5",
    "keywords": null,
    "creator": null,
    "description": "Plants, Fungi And Bacteria Working Together Mirage News",
    "content": "ONLY AVAILABLE IN PAID PLANS",
    "pubDate": "2025-04-15 22:21:00",
    "pubDateTZ": "UTC",
    "image_url": null,
    "video_url": null,
     "source":{  
        "source_id": "google",
        "source_name": "Google News",
        "source_priority": 14,
        "source_url": "https://news.google.com",
        "source_icon": "https://i.bytvi.com/domain_icons/google.png",
     }
    "language": "english",
    "country": [
            "australia"
         ],
    "category": [
        "science"
        ],
    "summary":"ai model will fill this feild"
    "views": 0
},

{....},
{....},
{....},

]



the below tag got with same api, bacouse this api will give only 10 articals then re-callapi with "nextPage": "1744755660618160752" this param to get more 10 articles and store in firebase.
I have 200/day calls gives 2000 articles.

https://newsdata.io/api/1/latest?apikey=pub_70272cd31c68fc8e897869b07c198e8221baf&removeduplicate=1&page=1744755660618160752

Above step will fill the data in firestore. But one feild still empty - "summary".

For this, 
1. After getting 10 articles store all neccessory data in firestore.
2. make a disconary in python contains {"article_id":"article_url"}.
3. collect all 10 articles urls into same discnary.
4. give this disc to my python function to create summary.
5. after getting 10 summaries a new python function will be store it into firestore with respective article_id and repeate fo next 10      articles.

----------------------------------------------------------------------
How python sumarry fuction works?
1. use from newspaper import articles -> use article url to extract text.
    ( I will use this text to train my ai model too.) 
2. pass this text to summary model (model_name = "csebuetnlp/mT5_multilingual_XLSum") who'll create summary.
    ( I will use this summary to train my ai model too.)
3. now we have summary, insert it into firestore. location => collection(news)->doc(article_id)->"summary":"this is summary"

4. also store this text and summary in a csv file to train my model in future. here is structure to save.


id,text,summary
1,"India has launched a new health mission aimed at improving medical infrastructure and accessibility in rural areas.","India launches health mission for rural areas."
2,"The government has announced new tax reforms to simplify the filing process and reduce rates for middle-income earners.","New tax reforms simplify filing and cut rates."
3,"A major earthquake struck Japan's eastern coast, causing significant damage but no tsunami warning was issued.","Earthquake hits Japan's east coast, no tsunami alert."
4,"Scientists have developed a new AI model that can detect early signs of cancer with higher accuracy.","AI model detects cancer early with better accuracy."
5,"Apple has unveiled its latest iPhone with advanced camera features and a faster processor.","Apple reveals new iPhone with better camera and speed."
6,"The Indian cricket team won the final match against Australia by 5 wickets, securing the tournament trophy.","India beats Australia to win cricket tournament."


5. We also kepp deleting data (articles from news collection(backend) and also from users-saved(its frontend's duty)) who was publised before 7 days.

6. Host on Renderand Start Executing all of this automatically at 12AM.

All set!!
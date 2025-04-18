# firestore_utils.py
import firebase_admin
from firebase_admin import credentials, firestore
import os
import json

def initialize_firestore():
    if not firebase_admin._apps:
       # Load credentials from environment
        cred_dict = json.loads(os.environ["GOOGLE_CREDENTIALS"])
        cred = credentials.Certificate(cred_dict)
        firebase_admin.initialize_app(cred)
    return firestore.client()

db = initialize_firestore()

def store_article(article):
    try:
        doc_id = article["article_id"]
        db.collection("news").document(doc_id).set(article)
        print(f"Stored article: {article.get('title', '')}")
    except Exception as e:
        print(f"Firestore Error for article {article.get('title', '')}: {e}")

# from fastapi import FastAPI, Form
# from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
# from newspaper import Article
# import pandas as pd
# import torch
# import os
# import csv

# app = FastAPI()

# # Load tokenizer and model
# model_name = "csebuetnlp/mT5_multilingual_XLSum"
# tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=False)
# model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

# csv_path = "summary_dataset.csv"

# def get_next_id():
#     if os.path.exists(csv_path):
#         df = pd.read_csv(csv_path)
#         if not df.empty and "id" in df.columns:
#             return df["id"].max() + 1
#     return 1

# @app.post("/summarize/")
# async def summarize_post(url: str = Form(...)):
#     # Extract article content
#     article = Article(url)
#     article.download()
#     article.parse()
#     text = article.text.strip()

#     #Clean the text to be single-line
#     cleaned_text = text.replace("\n", " ").replace("\r", " ").replace("\’","").replace("\‘","").replace("\‘‘","").replace("\’’","").strip()

#     # Tokenize and summarize
#     inputs = tokenizer.encode(cleaned_text, return_tensors="pt", truncation=True, max_length=512)
#     summary_ids = model.generate(
#         inputs,
#         max_length=150,
#         min_length=100,
#         length_penalty=2.0,
#         num_beams=4,
#         early_stopping=True
#     )
#     summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True).strip()

#     # Prepare data row
#     article_id = get_next_id()
#     df = pd.DataFrame([{
#         "id": article_id,
#         "text": cleaned_text,
#         "summary": "Anil"  # leave it empty
#     }])

#     # Save to CSV
#     df.to_csv(csv_path, mode='a', index=False, header=not os.path.exists(csv_path),quoting=csv.QUOTE_ALL)

#     return {"summary": summary}

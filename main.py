from fastapi import FastAPI
import nest_asyncio
from transformers import pipeline  # Import the pipeline function

sentiment_model = pipeline("text-classification", model="cardiffnlp/twitter-xlm-roberta-base-sentiment")     
app = FastAPI()

@app.get('/')
async def home():

  return "Welcome to Our FastAPI Endpoints"

@app.get('/sentiment_model/{text}')
async def home(text):

  return str(sentiment_model(text))


@app.get('/husnain')
async def home():

  return "Husnain is learning FastAPI."

ngrok_tunnel = ngrok.connect(8000)
print('Public URL:', ngrok_tunnel.public_url)
nest_asyncio.apply()
uvicorn.run(app, port=8000) 

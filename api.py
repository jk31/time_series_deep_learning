from fastapi import FastAPI

import yfinance as yf

app = FastAPI()

@app.get("/")
def root():
  return {"Hello": "World!"}


@app.get("/ticker/{ticker}")
def ticker(ticker):
  try:
    ticker = yf.Ticker(ticker.upper())
    data = ticker.info
    return data
  except:
    return {"error": "Ticker not found."}
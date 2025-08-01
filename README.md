#  Stock Market Stats API

A lightweight Python REST API that retrieves historical stock data using `yfinance`, computes basic financial statistics, and serves them via a FastAPI endpoint.

This project is part of the Tecta interview task for the Cloud & Backend internship.

---

##  Features

-  Pulls live historical stock data using `yfinance`
-  Calculates key figures: high, low, average close, and last close
-  Exposes a clean REST API with Swagger docs
-  Built with FastAPI
-  Fully containerized using Docker

---

##  Requirements

- Docker (recommended)
- OR: Python 3.11+ and `pip`

---

##  Example Endpoint

GET /api/stats?ticker=MSFT&start=2023-01-01&end=2023-12-31


##  Example Response:

---json
{
  "ticker": "MSFT",
  "start_date": "2023-01-03",
  "end_date": "2023-12-29",
  "high": 379.99,
  "low": 214.98,
  "average_close": 309.22,
  "last_close": 371.82
}

---json

## Running with Docker 

---docker
# Build the image
docker build -t stock-api .

# Run the container
docker run -d -p 8000:8000 stock-api
---docker

Then open this in your browser:
http://localhost:8000/docs

---

## Running Locally without Docker

pip install -r requirements.txt
uvicorn main:app --reload

Then open: http://localhost:8000/docs

---




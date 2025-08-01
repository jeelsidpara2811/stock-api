from fastapi import FastAPI, Query
from typing import Optional
import yfinance as yf
from datetime import datetime
import pandas as pd

app = FastAPI()

@app.get("/api/stats")
def get_stock_stats(
    ticker: str = Query(...),
    start: Optional[str] = None,
    end: Optional[str] = None
):
    try:
        # Fetch data
        data = yf.download(ticker, start=start, end=end)

        # Check if empty
        if data.empty:
            return {"error": f"No data found for ticker '{ticker}' in this range."}

        # Return clean stats
        return {
            "ticker": ticker.upper(),
            "start_date": str(data.index[0].date()),
            "end_date": str(data.index[-1].date()),
            "high": round(data['High'].max(), 2),
            "low": round(data['Low'].min(), 2),
            "average_close": round(data['Close'].mean(), 2),
            "last_close": round(data['Close'].iloc[-1], 2)
        }

    except Exception as e:
        return {"error": f"Server error: {str(e)}"}

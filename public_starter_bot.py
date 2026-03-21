"""
SCONZZ LAB | PUBLIC STARTER BOT
================================================
A basic, entry-level RSI Spot Trading algorithm. 
Note: This lacks the V4.2 Adaptive Memory Banks, 
100x routing, and 0% CPU mobile optimizations.
"""
import time, requests
import pandas as pd
import pandas_ta as ta

def fetch_market_data(symbol="SOLUSDT", interval="15m"):
    print(f"📡 Fetching data for {symbol}...")
    url = f"https://api.binance.com/api/v3/klines?symbol={symbol}&interval={interval}&limit=100"
    data = requests.get(url).json()
    df = pd.DataFrame(data, columns=['ts','o','h','l','c','v','ct','q','t','b','tq','i'])
    df['c'] = df['c'].astype(float)
    return df

def run_basic_bot():
    print("🟢 Sconzz Lab Starter Bot Online. Scanning 15m horizon...")
    position = None
    while True:
        try:
            df = fetch_market_data()
            df['rsi'] = ta.rsi(df['c'], length=14)
            curr_close = df['c'].iloc[-2]
            curr_rsi = df['rsi'].iloc[-2]
            print(f"Current Price: ${curr_close} | RSI: {curr_rsi:.2f}")

            if not position and curr_rsi < 30:
                print("⚡ Basic Signal: BUY (RSI Oversold)")
                position = "LONG"
            elif position and curr_rsi > 70:
                print("🎯 Basic Signal: SELL (RSI Overbought) - Profit Captured!")
                position = None
        except Exception as e:
            print("Error connecting to market.")
        time.sleep(60)

if __name__ == "__main__":
    run_basic_bot()

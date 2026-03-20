# ⚡ Sconzz LAB | Solana Quantitative Architecture

A complete, high-frequency quantitative trading floor built for the SOL/USDT market. Engineered by **Sconzz LAB**, this architecture features a Node.js execution engine, two distinct Python-based trading algorithms, and a built-in hyper-optimization lab for continuous backtesting. 

📍 **Base:** London, UK 🇬🇧

---

## 🏗️ System Architecture

The Sconzz LAB ecosystem is split into three main layers:
1. **The Execution Engine (server.js):** A Node.js backend that handles transaction routing, metric tracking, and the "Paper Trading" safety switch.
2. **The 100x Degen Bot (strategy_template.py):** An aggressive, 3-minute timeframe mean-reversion algorithm designed for choppy market regimes.
3. **The 20x Sniper Bot (strategy_template.py):** A highly precise, 5-minute timeframe liquidity sweep algorithm designed for institutional-style scalping.

*(Note: Proprietary alpha, optimization parameters, and API keys are strictly vaulted and not included in this public repository).*

### 🚀 Key Features
* **Dual-Speed Risk Manager:** Bots operate in "Hunter Mode" (checking charts every 15s) until they enter a trade, instantly shifting into "Sniper Mode" (checking live price every 2s) to execute risk management with absolute precision.
* **Auto-Compounding:** Automatically reinvests 50% of trade profits into the base trade size for exponential capital growth.
* **Hyper-Optimization Lab:** Custom Python scripts that backtest hundreds of configurations against thousands of historical candles to find the highest-yielding statistical edge.
* **Telegram Integration:** Real-time trade execution alerts, status polling, and live PnL tracking.

---

## 🛠️ Infrastructure

**Tech Stack:** Node.js | Python 3 | PM2 | Pandas-TA
**Environment:** Lightweight Linux/Termux headless server.

*This repository serves as a structural demonstration of the Sconzz LAB trading architecture.*

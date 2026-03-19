# ⚡ Sconzz LAB | The Mobile Quant Architecture

**Welcome to Sconzz LAB.** This repository is a public showcase of a high-frequency trading floor designed to scalp the Solana (SOL/USDT) perpetual futures market. 

The entire architecture is heavily optimized to run seamlessly in the background of a mobile device via Termux. No desktop. No cloud servers. Just pure algorithmic execution on the go.

### 🏛️ The Architecture
- **20x Sniper Engine:** Mean-reversion Python bot hunting volatility expansions.
- **100x Degen Engine:** High-speed momentum tracker.
- **Node.js Floor:** Headless execution server routing via Jupiter Perps.
- **Proprietary Optimizer (Black-Boxed):** A custom historical backtesting laboratory I built to stress-test my personal parameters. *Note: This is strictly for my private use and is not included in this repository.*

---

### ⏱️ 10-Minute Quickstart Guide
1. **Clone the Repo:** `git clone https://github.com/SconzzDen/Sconzz-LAB-Public.git`
2. **Install Dependencies:** `pip install -r requirements.txt` *(Note: create your own based on your indicators)*
3. **Configure Environment:** Add your Telegram Bot Token to the script.
4. **Run the Bot:** `python public_sniper_template.py`

### 🛑 CRITICAL: Paper Trading vs Live Mode
By default, this code ships in **TEST MODE** (`PAPER_TRADING = True`). It will only print simulated trades to your console. **No capital is at risk.**

To go live with real funds:
1. Open `public_sniper_template.py`.
2. Find line 14: `PAPER_TRADING = True`.
3. Change it to `PAPER_TRADING = False`.
4. Inject your exchange API keys into the `execute_trade` function.

### ⚠️ Disclaimer
**This repository contains structural templates only.** The proprietary trading logic (Alpha) and my personal optimization engines have been removed. You **must** write your own mathematical indicators and build your own backtester to prove your edge before putting capital at risk. I am not responsible for any financial losses incurred by using this framework. 

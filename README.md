# ⚡ Sconzz LAB | Quantitative Trading Architecture

**Welcome to Sconzz LAB.** This repository is a public showcase of a high-frequency, dual-engine trading floor designed to scalp the Solana (SOL/USDT) perpetual futures market via the Jupiter protocol. 

A major engineering focus of this project was extreme resource efficiency. The entire architecture is heavily optimized to run seamlessly in the background of a mobile device via Termux. No desktop required. No expensive cloud servers. Just pure, uninterrupted algorithmic execution on the go.

### 🏛️ The Architecture

- **The Brain (Python):** Custom mathematical indicators (Bollinger Band sweeps, RSI) process live market data to generate precision buy/sell signals.
- **The Floor (Node.js):** A headless JavaScript execution engine that catches the Python signals and securely routes them through the Solana blockchain using Jupiter Perps.
- **The Comms (Telegram API):** A private Telegram Control Matrix allows for real-time risk adjustments, bot pausing, and PnL reporting via encrypted DMs.
- **The Immortal Engine (PM2):** Custom wake-locks and boot scripts ensure the bot survives mobile battery optimizers and automatically resurrects upon device reboot.

### 🤖 The Bots
1. **20x Sniper:** A calculated, mean-reversion engine hunting for specific volatility expansions.
2. **100x Degen:** A high-speed, aggressive momentum tracker built for extreme liquidity events.

---

### 🔒 Why is the core logic black-boxed?

**This repository contains structural templates only.** The actual `bot.py` containing the proprietary trading logic (Alpha), the execution engine (`server.js`), and the `.env` vaults containing private keys are strictly locked in an isolated, private repository. 

What you see here is the *skeleton* of Sconzz LAB, demonstrating the engineering framework and mobile optimization without exposing the proprietary edge.

# binance-trading-bot

# 💹 Binance Futures Testnet Crypto Trading Bot

This project is a simplified crypto trading bot built as part of the hiring process for the **Junior Python Developer – Crypto Trading Bot** role at Bajarangs / PrimeTrade.AI.

---

## 📌 Features

- ✅ Place `MARKET` and `LIMIT` orders on **Binance Futures Testnet**
- ✅ Supports both `BUY` and `SELL` sides
- ✅ Validates user input via command-line interface
- ✅ Implements logging to `bot.log`
- ✅ Handles API errors and invalid inputs gracefully
- ✅ Configurable to support Stop-Limit/OCO in future

---

## 🚀 How It Works

The bot uses the `python-binance` library to interact with Binance's USDT-M Futures Testnet.

### Input via CLI:
- Trading Pair (e.g., BTCUSDT)
- Side (BUY/SELL)
- Order Type (MARKET/LIMIT)
- Quantity (e.g., 0.01)

---

## 🔧 Requirements

- Python 3.7+
- `python-binance` library

### Install dependencies:
```bash
pip install python-binance

# bot.py
from binance.client import Client
from binance.enums import *
import logging
import time
from config import API_KEY, API_SECRET

# Set up logging
logging.basicConfig(filename='bot.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True):
        self.client = Client(api_key, api_secret)
        if testnet:
            self.client.API_URL = 'https://testnet.binancefuture.com/fapi'  # For futures
            self.client.FUTURES_URL = 'https://testnet.binancefuture.com/fapi'
        logging.info("Initialized Binance Client")

    def place_order(self, symbol, side, order_type, quantity, price=None):
        try:
            if order_type == "MARKET":
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type=ORDER_TYPE_MARKET,
                    quantity=quantity
                )
            elif order_type == "LIMIT":
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type=ORDER_TYPE_LIMIT,
                    timeInForce=TIME_IN_FORCE_GTC,
                    quantity=quantity,
                    price=price
                )
            else:
                raise ValueError("Unsupported order type")

            logging.info(f"Order placed: {order}")
            print("✅ Order placed successfully.")
            print(order)
        except Exception as e:
            logging.error(f"Order failed: {e}")
            print(f"❌ Error: {e}")

    def place_oco_order(self, symbol, quantity, take_profit_price, stop_price, stop_limit_price):
        try:
            # NOTE: OCO orders are **only supported on SPOT markets**, not Futures
            order = self.client.create_oco_order(
                symbol=symbol,
                side=SIDE_SELL,
                quantity=quantity,
                price=str(take_profit_price),
                stopPrice=str(stop_price),
                stopLimitPrice=str(stop_limit_price),
                stopLimitTimeInForce=TIME_IN_FORCE_GTC
            )
            logging.info(f"OCO Order placed: {order}")
            print("✅ OCO Order placed successfully.")
            print(order)
        except Exception as e:
            logging.error(f"OCO order failed: {e}")
            print(f"❌ Error placing OCO order: {e}")


def main():
    bot = BasicBot(API_KEY, API_SECRET)

    print("\n📊 Binance Trading Bot - Choose Order Type")
    print("1. MARKET Order")
    print("2. LIMIT Order")
    print("3. OCO Order (Bonus - Spot Only)")
    choice = input("Enter order type (1/2/3): ").strip()

    symbol = input("Enter trading pair (e.g. BTCUSDT): ").upper()

    if choice == '1' or choice == '2':
        side_input = input("Buy or Sell? (buy/sell): ").lower()
        quantity = float(input("Enter quantity: "))
        side = SIDE_BUY if side_input == "buy" else SIDE_SELL

        if choice == '2':
            price = input("Enter limit price: ")
            bot.place_order(symbol, side, "LIMIT", quantity, price)
        else:
            bot.place_order(symbol, side, "MARKET", quantity)

    elif choice == '3':
        print("\n⚠️ OCO orders work only on SPOT market, not FUTURES")
        quantity = float(input("Enter quantity: "))
        take_profit_price = float(input("Enter Take Profit Price: "))
        stop_price = float(input("Enter Stop Price: "))
        stop_limit_price = float(input("Enter Stop Limit Price: "))

        bot.place_oco_order(symbol, quantity, take_profit_price, stop_price, stop_limit_price)

    else:
        print("❌ Invalid choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()

import logging
from bot.client import BinanceFuturesClient
from bot.validators import (
    validate_symbol, validate_side, validate_order_type,
    validate_quantity, validate_price
)

logger = logging.getLogger(__name__)


class OrderManager:
    """Manages order placement on Binance Futures."""
    
    def __init__(self, api_key, api_secret):
        self.client = BinanceFuturesClient(api_key, api_secret)
    
    def place_order(self, symbol, side, order_type, quantity, price=None):
        """Place an order on Binance Futures Testnet.
        
        Args:
            symbol: Trading pair (e.g., BTCUSDT)
            side: BUY or SELL
            order_type: MARKET or LIMIT
            quantity: Order quantity
            price: Order price (required for LIMIT orders)
        
        Returns:
            dict: Order response from Binance API
        """
        # Validate inputs
        symbol = validate_symbol(symbol)
        side = validate_side(side)
        order_type = validate_order_type(order_type)
        quantity = validate_quantity(quantity)
        
        if order_type == 'LIMIT':
            if price is None:
                raise ValueError("Price is required for LIMIT orders")
            price = validate_price(price)
        
        # Build order parameters
        params = {
            'symbol': symbol,
            'side': side,
            'type': order_type,
            'quantity': quantity
        }
        
        if order_type == 'LIMIT':
            params['price'] = price
            params['timeInForce'] = 'GTC'  # Good Till Cancel
        
        # Log order summary
        logger.info("=" * 60)
        logger.info("ORDER REQUEST SUMMARY")
        logger.info("=" * 60)
        for key, value in params.items():
            logger.info(f"{key}: {value}")
        logger.info("=" * 60)
        
        print("\n" + "=" * 60)
        print("ORDER REQUEST SUMMARY")
        print("=" * 60)
        for key, value in params.items():
            print(f"{key}: {value}")
        print("=" * 60 + "\n")
        
        # Place the order
        try:
            response = self.client._make_request(
                'POST',
                '/fapi/v1/order',
                params=params,
                signed=True
            )
            
            # Log and print response
            logger.info("=" * 60)
            logger.info("ORDER RESPONSE")
            logger.info("=" * 60)
            logger.info(f"Order ID: {response.get('orderId')}")
            logger.info(f"Status: {response.get('status')}")
            logger.info(f"Executed Qty: {response.get('executedQty')}")
            logger.info(f"Avg Price: {response.get('avgPrice', 'N/A')}")
            logger.info("=" * 60)
            
            print("\n" + "=" * 60)
            print("ORDER RESPONSE")
            print("=" * 60)
            print(f"Order ID: {response.get('orderId')}")
            print(f"Client Order ID: {response.get('clientOrderId')}")
            print(f"Symbol: {response.get('symbol')}")
            print(f"Status: {response.get('status')}")
            print(f"Side: {response.get('side')}")
            print(f"Type: {response.get('type')}")
            print(f"Executed Qty: {response.get('executedQty')}")
            print(f"Cumulative Quote Qty: {response.get('cumQuote', 'N/A')}")
            print(f"Avg Price: {response.get('avgPrice', 'N/A')}")
            print("=" * 60)
            print("\n✅ Order placed successfully!\n")
            
            return response
            
        except Exception as e:
            logger.error(f"Failed to place order: {e}")
            print(f"\n❌ Order failed: {e}\n")
            raise

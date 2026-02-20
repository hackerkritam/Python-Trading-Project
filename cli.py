#!/usr/bin/env python3
"""Trading Bot CLI for Binance Futures Testnet"""

import argparse
import sys
import os
from bot.logging_config import setup_logging
from bot.orders import OrderManager


def main():
    """Main CLI entry point."""
    # Setup logging
    logger = setup_logging()
    logger.info("Trading bot started")
    
    # Parse command line arguments
    parser = argparse.ArgumentParser(
        description='Trading Bot for Binance Futures Testnet',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Place a market buy order
  python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
  
  # Place a limit sell order
  python cli.py --symbol ETHUSDT --side SELL --type LIMIT --quantity 0.01 --price 3500

Environment Variables:
  BINANCE_API_KEY     Your Binance Futures Testnet API key
  BINANCE_API_SECRET  Your Binance Futures Testnet API secret
"""
    )
    
    parser.add_argument('--symbol', required=True, 
                       help='Trading symbol (e.g., BTCUSDT)')
    parser.add_argument('--side', required=True, 
                       choices=['BUY', 'SELL', 'buy', 'sell'],
                       help='Order side')
    parser.add_argument('--type', required=True, 
                       choices=['MARKET', 'LIMIT', 'market', 'limit'],
                       help='Order type')
    parser.add_argument('--quantity', required=True, type=float,
                       help='Order quantity')
    parser.add_argument('--price', type=float,
                       help='Order price (required for LIMIT orders)')
    
    args = parser.parse_args()
    
    # Get API credentials from environment
    api_key = os.getenv('BINANCE_API_KEY')
    api_secret = os.getenv('BINANCE_API_SECRET')
    
    if not api_key or not api_secret:
        print("\n❌ Error: API credentials not found!")
        print("Please set BINANCE_API_KEY and BINANCE_API_SECRET environment variables.\n")
        logger.error("Missing API credentials")
        sys.exit(1)
    
    try:
        # Initialize order manager
        order_manager = OrderManager(api_key, api_secret)
        
        # Place the order
        order_manager.place_order(
            symbol=args.symbol,
            side=args.side,
            order_type=args.type,
            quantity=args.quantity,
            price=args.price
        )
        
        logger.info("Trading bot completed successfully")
        
    except ValueError as e:
        print(f"\n❌ Validation Error: {e}\n")
        logger.error(f"Validation error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error: {e}\n")
        logger.error(f"Unexpected error: {e}", exc_info=True)
        sys.exit(1)


if __name__ == '__main__':
    main()

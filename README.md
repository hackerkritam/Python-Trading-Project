# Trading Bot - Binance Futures Testnet

A clean, production-ready Python trading bot for placing orders on Binance Futures Testnet (USDT-M).

## Features

- ✅ Place MARKET and LIMIT orders
- ✅ Support for BUY and SELL sides
- ✅ Comprehensive input validation
- ✅ Structured logging to file and console
- ✅ Clean error handling
- ✅ Reusable client architecture

## Setup

### 1. Prerequisites

- Python 3.8+
- Binance Futures Testnet account ([Register here](https://testnet.binancefuture.com))

### 2. Installation

```bash
# Clone the repository
git clone <your-repo-url>
cd trading_bot

# Install dependencies
pip install -r requirements.txt
```

### 3. Configuration

Set your API credentials as environment variables:

**Windows (CMD):**
```cmd
set BINANCE_API_KEY=your_api_key_here
set BINANCE_API_SECRET=your_api_secret_here
```

**Windows (PowerShell):**
```powershell
$env:BINANCE_API_KEY="your_api_key_here"
$env:BINANCE_API_SECRET="your_api_secret_here"
```

**Linux/Mac:**
```bash
export BINANCE_API_KEY=your_api_key_here
export BINANCE_API_SECRET=your_api_secret_here
```

## Usage

### Basic Commands

Place a MARKET order:
```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

Place a LIMIT order:
```bash
python cli.py --symbol ETHUSDT --side SELL --type LIMIT --quantity 0.01 --price 3500
```

### Command Line Arguments

- `--symbol`: Trading pair (e.g., BTCUSDT, ETHUSDT)
- `--side`: Order side (BUY or SELL)
- `--type`: Order type (MARKET or LIMIT)
- `--quantity`: Order quantity (float)
- `--price`: Order price (required for LIMIT orders)

## Project Structure

```
trading_bot/
├── bot/
│   ├── __init__.py          # Package initialization
│   ├── client.py            # Binance API client wrapper
│   ├── orders.py            # Order placement logic
│   ├── validators.py        # Input validation functions
│   └── logging_config.py    # Logging configuration
├── cli.py                   # CLI entry point
├── requirements.txt         # Python dependencies
├── README.md               # This file
└── logs/                   # Auto-generated log files
```

## Logging

All operations are logged to:
- Console (stdout)
- Log files in `logs/` directory with timestamp

Each log file contains:
- Request parameters
- API responses
- Errors and exceptions
- Timestamps for all operations

## Error Handling

The bot handles:
- Invalid input validation
- API errors (rate limits, insufficient balance, etc.)
- Network failures
- Authentication errors

## Testing Examples

### Example 1: Market Buy Order
```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### Example 2: Limit Sell Order
```bash
python cli.py --symbol ETHUSDT --side SELL --type LIMIT --quantity 0.01 --price 3500
```

## Assumptions

- Using Binance Futures Testnet (USDT-M contracts)
- All symbols are USDT pairs
- LIMIT orders use GTC (Good Till Cancel) time in force
- Testnet base URL: https://testnet.binancefuture.com

## Notes

- This is for TESTNET only - no real funds are used
- Make sure your testnet account has sufficient balance
- API keys are for testnet and won't work on production

## License

MIT

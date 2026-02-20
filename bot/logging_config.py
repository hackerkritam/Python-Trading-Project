import logging
import os
from datetime import datetime


def setup_logging():
    """Configure logging for the trading bot."""
    if not os.path.exists('logs'):
        os.makedirs('logs')
    
    log_filename = f"logs/trading_bot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_filename),
            logging.StreamHandler()
        ]
    )
    
    return logging.getLogger(__name__)

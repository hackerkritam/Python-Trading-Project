import logging

logger = logging.getLogger(__name__)


def validate_symbol(symbol):
    """Validate trading symbol format."""
    if not symbol or not isinstance(symbol, str):
        raise ValueError("Symbol must be a non-empty string")
    
    symbol = symbol.upper().strip()
    
    if not symbol.endswith('USDT'):
        logger.warning(f"Symbol {symbol} doesn't end with USDT - might not be valid for USDT-M futures")
    
    return symbol


def validate_side(side):
    """Validate order side."""
    valid_sides = ['BUY', 'SELL']
    side = side.upper().strip()
    
    if side not in valid_sides:
        raise ValueError(f"Side must be one of {valid_sides}")
    
    return side


def validate_order_type(order_type):
    """Validate order type."""
    valid_types = ['MARKET', 'LIMIT']
    order_type = order_type.upper().strip()
    
    if order_type not in valid_types:
        raise ValueError(f"Order type must be one of {valid_types}")
    
    return order_type


def validate_quantity(quantity):
    """Validate order quantity."""
    try:
        qty = float(quantity)
        if qty <= 0:
            raise ValueError("Quantity must be positive")
        return qty
    except (ValueError, TypeError):
        raise ValueError("Quantity must be a valid positive number")


def validate_price(price):
    """Validate order price."""
    if price is None:
        return None
    
    try:
        p = float(price)
        if p <= 0:
            raise ValueError("Price must be positive")
        return p
    except (ValueError, TypeError):
        raise ValueError("Price must be a valid positive number")

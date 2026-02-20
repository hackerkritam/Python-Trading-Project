import logging
import hmac
import hashlib
import time
import requests
from urllib.parse import urlencode

logger = logging.getLogger(__name__)


class BinanceFuturesClient:
    """Client for interacting with Binance Futures Testnet API."""
    
    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret
        self.base_url = "https://testnet.binancefuture.com"
        self.session = requests.Session()
        self.session.headers.update({'X-MBX-APIKEY': self.api_key})
    
    def _generate_signature(self, params):
        """Generate HMAC SHA256 signature for authenticated requests."""
        query_string = urlencode(params)
        signature = hmac.new(
            self.api_secret.encode('utf-8'),
            query_string.encode('utf-8'),
            hashlib.sha256
        ).hexdigest()
        return signature
    
    def _make_request(self, method, endpoint, params=None, signed=False):
        """Make HTTP request to Binance API."""
        url = f"{self.base_url}{endpoint}"
        
        if params is None:
            params = {}
        
        if signed:
            params['timestamp'] = int(time.time() * 1000)
            params['recvWindow'] = 60000  # 60 seconds window
            params['signature'] = self._generate_signature(params)
        
        logger.info(f"Making {method} request to {endpoint}")
        logger.debug(f"Request params: {params}")
        
        try:
            if method == 'GET':
                response = self.session.get(url, params=params)
            elif method == 'POST':
                response = self.session.post(url, params=params)
            else:
                raise ValueError(f"Unsupported HTTP method: {method}")
            
            response.raise_for_status()
            data = response.json()
            
            logger.info(f"Response received: {response.status_code}")
            logger.debug(f"Response data: {data}")
            
            return data
            
        except requests.exceptions.HTTPError as e:
            logger.error(f"HTTP error occurred: {e}")
            logger.error(f"Response: {e.response.text}")
            raise
        except requests.exceptions.RequestException as e:
            logger.error(f"Network error occurred: {e}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            raise
    
    def test_connectivity(self):
        """Test API connectivity."""
        return self._make_request('GET', '/fapi/v1/ping')
    
    def get_exchange_info(self):
        """Get exchange trading rules and symbol information."""
        return self._make_request('GET', '/fapi/v1/exchangeInfo')
    
    def get_account_info(self):
        """Get current account information."""
        return self._make_request('GET', '/fapi/v2/account', signed=True)

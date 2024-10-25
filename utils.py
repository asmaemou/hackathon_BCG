import requests
import time
import hmac
import hashlib
import base64
import json
from fastapi import HTTPException
from models import RequestData
from config import GEMINI_API_KEY, GEMINI_API_SECRET_ENCODED, GEMINI_API_URL

def place_order_util(request_data: RequestData):
    try:
        endpoint = "/v1/order/new"
        url = GEMINI_API_URL + endpoint

        payload = {
            "request": endpoint,
            "nonce": str(int(time.time() * 1000)),
            "symbol": request_data.symbol,
            "amount": request_data.amount,
            "price": request_data.price,
            "side": request_data.side,
            "type": request_data.order_type
        }

        encoded_payload = json.dumps(payload).encode()
        b64 = base64.b64encode(encoded_payload)
        signature = hmac.new(GEMINI_API_SECRET_ENCODED, b64, hashlib.sha384).hexdigest()

        headers = {
            'Content-Type': 'text/plain',
            'Content-Length': '0',
            'X-GEMINI-APIKEY': GEMINI_API_KEY,
            'X-GEMINI-PAYLOAD': b64.decode(),
            'X-GEMINI-SIGNATURE': signature,
            'Cache-Control': 'no-cache'
        }

        response = requests.post(url, headers=headers)
        response.raise_for_status()
        return response.json()

    except requests.exceptions.HTTPError as errh:
        error_message = response.json().get('message', str(errh))
        raise HTTPException(status_code=response.status_code, detail=error_message)
    except requests.exceptions.RequestException as err:
        raise HTTPException(status_code=500, detail=str(err))

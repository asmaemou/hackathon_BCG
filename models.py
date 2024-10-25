from pydantic import BaseModel

class RequestData(BaseModel):
    symbol: str
    amount: str
    price: str
    side: str  # "buy" or "sell"
    order_type: str  # e.g., "exchange limit"

class ResponseData(BaseModel):
    order_id: str
    symbol: str
    exchange: str
    price: str
    avg_execution_price: str
    side: str
    type: str
    timestamp: str
    is_live: bool
    is_cancelled: bool
    executed_amount: str
    remaining_amount: str
    original_amount: str

# API Docs
**URL:** https://orders-rmq-broker-production.up.railway.app
**Swagger:**https://orders-rmq-broker-production.up.railway.app/docs
## Methods:
### POST /api/orders/push/
**data:**
{
  "client": "string",
  "number": "string",
  "date": "string",
  "status": "string",
  "amount": float,
  "pay_link": "string",
  "pay_status": "string",
  "cooking_time_from": "string",
  "cooking_time_to": "string",
  "delivery_time_from": "string",
  "delivery_time_to": "string",
  "project": "string",
  "trade_point": "string",
  "trade_point_card": "string",
  "delivery_method": "string",
  "delivery_adress": "string",
  "phones": ["string"]
}

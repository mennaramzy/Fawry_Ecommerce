
# Fawry E-Commerce System

## Assumptions
- All prices are in EGP.
- Flat shipping fee of 30 EGP is charged if at least one shippable item exists.
- Perishable products are rejected if expired.
- Cart items must not exceed available stock.
- System runs in terminal only.

## Features
- Item class supports optional expiry and shipping attributes.
- User class maintains balance.
- ShoppingCart allows adding items with validation.
- DeliveryService calculates weight and prints shipping notice.
- Checkout process handles all constraints and prints full receipt.

## Corner Cases Tested
1. Empty cart
2. Insufficient balance
3. Expired product
4. Quantity greater than stock
5. Valid order including shipping and non-shipping items

## How to Run
- Save the code in `main.py`
- Run via terminal:
  python main.py


TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "search_menu",
            "description": "Search the restaurant menu for items matching a query",
            "parameters": {
                "type": "object",
                "properties": {"query": {"type": "string"}},
                "required": ["query"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "add_to_cart",
            "description": "Add an item to the customer's cart",
            "parameters": {
                "type": "object",
                "properties": {
                    "item_id": {"type": "string"},
                    "quantity": {"type": "integer"}
                },
                "required": ["item_id", "quantity"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "calculate_total",
            "description": "Calculate the total price of everything currently in the cart",
            "parameters": {"type": "object", "properties": {}}
        }
    },
    {
        "type": "function",
        "function": {
            "name": "create_order",
            "description": "Finalize the cart into an order once the customer confirms and has given a delivery address",
            "parameters": {
                "type": "object",
                "properties": {
                    "delivery_address": {"type": "string", "description": "The customer's delivery address or location"}
                },
                "required": ["delivery_address"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "generate_payment_link",
            "description": "Generate a UPI payment link for the given order total",
            "parameters": {
                "type": "object",
                "properties": {"amount": {"type": "number"}},
                "required": ["amount"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "notify_restaurant",
            "description": "Send the confirmed order details to the restaurant",
            "parameters": {"type": "object", "properties": {}}
        }
    }
]
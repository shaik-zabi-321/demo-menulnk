from menu import MENU

# Simple in-memory session state (fine for a demo, not for production)
session = {"cart": [], "restaurant": "spice_house", "last_order": {}}

def search_menu(query):
    items = MENU[session["restaurant"]]["items"]
    matches = [i for i in items if query.lower() in i["name"].lower()]
    return {"results": matches if matches else items}

def add_to_cart(item_id, quantity):
    items = MENU[session["restaurant"]]["items"]
    item = next((i for i in items if i["id"] == item_id), None)
    if not item:
        return {"error": "item not found"}
    session["cart"].append({**item, "quantity": quantity})
    return {"cart": session["cart"]}

def calculate_total():
    total = sum(i["price"] * i["quantity"] for i in session["cart"])
    return {"total": total}

def create_order():
    total = sum(i["price"] * i["quantity"] for i in session["cart"])
    order = {"order_id": "ORD1042", "items": session["cart"].copy(), "total": total}
    session["last_order"] = order   # remember this order before clearing the cart
    session["cart"] = []            # reset the cart now that the order is placed
    return order

def generate_payment_link(amount):
    # Fake link for demo purposes — real UPI integration is a separate project
    return {"payment_link": f"upi://pay/SpiceHouse@upi?amount={amount}"}

def notify_restaurant():
    # In a real system this would hit the restaurant's dashboard/notification
    order = session.get("last_order", {})
    print(f"[NOTIFY] New order for {session['restaurant']}: {order}")
    return {"status": "restaurant notified"}

HANDLERS = {
    "search_menu": lambda i: search_menu(i["query"]),
    "add_to_cart": lambda i: add_to_cart(i["item_id"], i["quantity"]),
    "calculate_total": lambda i: calculate_total(),
    "create_order": lambda i: create_order(),
    "generate_payment_link": lambda i: generate_payment_link(i["amount"]),
    "notify_restaurant": lambda i: notify_restaurant(),
}